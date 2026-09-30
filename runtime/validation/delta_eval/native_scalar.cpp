// Direct native eval_node corroboration; no Python-authored compute node.
#include <hgraph/lib/testing/eval_node.h>
#include <hgraph/types/static_node.h>
#include "../fixed/native_loaded_libraries.h"
#include <iomanip>
#include <iostream>
#include <optional>
#include <string>
#include <vector>
using namespace hgraph;
#define PASS_NODE(N,T) struct N { static constexpr auto name = #N; \
 static void eval(In<"ts",TS<T>> ts,Out<TS<T>> out) { out.apply(ts.delta_value()); } };
PASS_NODE(PassBool,Bool)
PASS_NODE(PassInt,Int)
PASS_NODE(PassFloat,Float)
PASS_NODE(PassStr,Str)
PASS_NODE(PassDate,Date)
PASS_NODE(PassTime,Time)
PASS_NODE(PassDateTime,DateTime)
PASS_NODE(PassDuration,TimeDelta)
void print(Bool v) { std::cout << (v?"true":"false"); }
void print(Int v) { std::cout << v; }
void print(Float v) { std::cout << std::setprecision(17) << v; }
void print(const Str &v) { std::cout << std::quoted(v); }
void print(Date v) { std::cout << std::chrono::sys_days(v).time_since_epoch().count(); }
void print(Time v) { std::cout << v.microseconds; }
void print(DateTime v) { std::cout << v.time_since_epoch().count(); }
void print(TimeDelta v) { std::cout << v.count(); }
bool first=true;
template<class Node,class T>
void run(const std::string &name,T a,T b) {
 using V=std::vector<std::optional<T>>;
 const std::optional<T> idle{};
 const std::vector<std::pair<std::string,V>> cases{
  {"equal_distinct",{a,a,b,a}},
  {"silence",{idle,idle,a,idle,a,b,idle,idle,a,idle,idle}},
  {"all_silent",{idle,idle,idle,idle}},
  {"empty",{}}};
 for(const auto &[suffix,input]:cases) {
  const auto result=hgraph::testing::eval_node<Node>(input);
  if(!first) { std::cout << ','; }
  first=false;
  std::cout << std::quoted(name+"_"+suffix) << ":[";
  bool first_value=true;
  for(const auto &value:result) {
   if(!first_value) { std::cout << ','; }
   first_value=false;
   if(value) print(*value); else std::cout << "null";
  }
  std::cout << ']';
 }
}
int main() {
 try {
  std::cout << "{\"source_sha256\":\"" << DELTA_SOURCE_SHA256 << "\",\"observed\":{";
  run<PassBool>("bool",false,true);
  run<PassInt>("i64",Int{0},Int{-7});
  run<PassFloat>("f64",Float{0},Float{1.5});
  run<PassStr>("str",Str{},Str{"delta"});
  const Date epoch=std::chrono::year{1970}/1/1;
  const Date leap=std::chrono::year{2024}/2/29;
  run<PassDate>("date",epoch,leap);
  run<PassTime>("time",Time{0},time_of_day(12,34,56));
  run<PassDateTime>("datetime",DateTime{},DateTime{std::chrono::sys_days(leap)}+std::chrono::hours{12}+std::chrono::minutes{34}+std::chrono::seconds{56});
  run<PassDuration>("duration",TimeDelta{0},TimeDelta{1000000});
  std::cout << "},\"libraries\":[";
  bool first_library=true;
  for(const auto &path:loaded_libraries()) if(path.find("hgraph")!=std::string::npos) {
   if(!first_library) { std::cout << ','; }
   first_library=false;
   std::cout << std::quoted(path);
  }
  std::cout << "]}\n";
 } catch(const std::exception &e) { std::cerr << e.what() << '\n'; return 1; }
}
