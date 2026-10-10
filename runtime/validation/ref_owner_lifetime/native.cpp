#include <hgraph/lib/testing/eval_node.h>
#include <hgraph/lib/std/std_operators.h>
#include <hgraph/lib/std/std_nodes.h>
#include <hgraph/types/static_node.h>
#include "../fixed/native_loaded_libraries.h"
#include <compare>
#include <iomanip>
#include <iostream>
#include <optional>
#include <string>
#include <vector>
using namespace hgraph;
struct Producer {
 static constexpr auto name="producer";
 static void eval(In<"value",TS<Int>> value, Out<TS<Int>> out) { out.set(value.value()); }
};
struct Relay {
 static constexpr auto name="relay";
 static void eval(In<"value",TS<Int>> value, Out<REF<TS<Int>>> out) { out.set(value.reference()); }
};
template<bool Own> struct Branch {
 static Port<REF<TS<Int>>> compose(Wiring &w, Port<TS<Int>> value) {
  if constexpr(Own) return wire<Relay>(w,wire<Producer>(w,value));
  else return wire<Relay>(w,value);
 }
};
struct First {
 static constexpr auto name="first";
 static void eval(In<"value",REF<TS<Int>>> value, State<Bool> done, Out<REF<TS<Int>>> out) {
  if(!done.get()) { done.set(true); out.set(value.value()); }
 }
};
struct Observe {
 static constexpr auto name="observe";
 static void eval(In<"reference",REF<TS<Int>>,InputActivity::Passive,InputValidity::Unchecked> reference,
                  In<"data",TS<Int>,InputActivity::Passive,InputValidity::Unchecked> data,
                  In<"step",TS<Int>>, Out<TS<Str>> out) {
  out.set(std::string("{\"reference_valid\":")+(reference.valid()?"true":"false")+
    ",\"reference_modified\":"+(reference.modified()?"true":"false")+
    ",\"data_valid\":"+(data.valid()?"true":"false")+
    ",\"data_modified\":"+(data.modified()?"true":"false")+
    ",\"value\":"+(data.valid()?std::to_string(data.value()):"null")+"}");
 }
};
template<bool Own> struct Graph {
 static Port<TS<Str>> compose(Wiring &w,Port<TS<Str>> key,Port<TS<Int>> value,Port<TS<Int>> step) {
  auto selected=wire<stdlib::switch_>(w,key,stdlib::switch_cases({{Value{Str{"a"}},fn<Branch<Own>>()},{Value{Str{"b"}},fn<Branch<Own>>()}}),value).template as<REF<TS<Int>>>();
  auto held=wire<First>(w,selected);
  return wire<Observe>(w,held,held.template as<TS<Int>>(),step);
 }
};
struct Identity {
 static constexpr auto name="identity";
 static void eval(In<"first",REF<TS<Int>>> first,In<"same",REF<TS<Int>>> same,In<"distinct",REF<TS<Int>>> distinct,Out<TS<Str>> out) {
  out.set(std::string("{\"same_endpoint\":")+(first.value()==same.value()?"true":"false")+",\"distinct_equal_endpoints\":"+(first.value()==distinct.value()?"true":"false")+"}");
 }
};
struct IdentityGraph {
 static Port<TS<Str>> compose(Wiring &w,Port<TS<Int>> first,Port<TS<Int>> second) {
  auto a=wire<Relay>(w,first);auto b=wire<Relay>(w,second);
  return wire<Identity>(w,a,a,b);
 }
};
int main() {
 try {
  stdlib::register_standard_operators();
  std::vector<std::optional<Str>> keys={"a","a","b","b","a","a"};
  std::vector<std::optional<Int>> values={7,8,20,21,9,10},steps={1,1,1,1,1,1};
  auto rows=[](auto rows) { std::cout<<'[';bool first=true;for(const auto &row:rows) {if(!first)std::cout<<',';first=false;if(row)std::cout<<*row;else std::cout<<"null";}std::cout<<']';};
  std::cout<<"{\"source_sha256\":"<<std::quoted(SOURCE_SHA256)<<",\"owned\":";
  rows(testing::eval_node<Graph<true>>(keys,values,steps));
  std::cout<<",\"outer_owner_control\":";rows(testing::eval_node<Graph<false>>(keys,values,steps));
  std::cout<<",\"identity\":";rows(testing::eval_node<IdentityGraph>(std::vector<std::optional<Int>>{7},std::vector<std::optional<Int>>{7}));
  Value f{false},t{true},other{false};
  std::cout<<",\"bool_operations\":{\"false_before_true\":"<<(f.compare(t)==std::partial_ordering::less?"true":"false")<<",\"equal_false_hash\":"<<(f.equals(other)&&f.hash()==other.hash()?"true":"false")<<"},\"libraries\":[";
  bool first=true;for(const auto &path:loaded_libraries()) {if(std::filesystem::path(path).filename().string().find("hgraph")==std::string::npos)continue;if(!first)std::cout<<',';first=false;std::cout<<std::quoted(path);}std::cout<<"]}\n";
 }catch(const std::exception &e){std::cerr<<e.what()<<'\n';return 1;}
}
