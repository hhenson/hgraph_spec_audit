#include <hgraph/lib/testing/eval_node.h>
#include <hgraph/runtime/global_state.h>
#include <hgraph/types/static_node.h>
#include <hgraph/types/value/value_builder.h>
#include "../fixed/native_loaded_libraries.h"
#include <iomanip>
#include <iostream>
using namespace hgraph;

Value list(std::initializer_list<Int> items) {
 auto &r=TypeRegistry::instance();
 Value v{ValuePlanFactory::instance().type_for(r.mutable_list(scalar_descriptor<Int>::value_meta()))};
 auto m=v.as_list().begin_mutation();
 for(auto x:items) { m.push_back(Value{x}.view()); }
 return v;
}
void append(const ValueView &v,Int x) {v.as_list().begin_mutation().push_back(Value{x}.view());}
void print_list(const ValueView &v) {
 std::cout << '[';const auto l=v.as_list();
 for(std::size_t i=0;i<l.size();++i) {
  if(i) {std::cout << ',';}
  const auto x=l.at(i);
  if(x.is_list()) {print_list(x);} else {std::cout << x.checked_as<Int>();}
 }
 std::cout << ']';
}
bool first=true;
void field(const char *name,const ValueView &v) {
 if(!first) {std::cout << ',';} first=false;
 std::cout << std::quoted(name) << ':';print_list(v);
}
void textfield(const char *name,const std::string &value) {
 if(!first) {std::cout << ',';} first=false;
 std::cout << std::quoted(name) << ':' << std::quoted(value);
}
struct TimedSource {
 static constexpr auto name="ordinary_timed_list_source";
 static constexpr bool schedule_on_start=true;
 static void eval(Scalar<"data",ScalarVar<"D">> data,State<Int> cursor,NodeScheduler sched,DateTime now,Out<TS<Int>> out) {
  const auto rows=data.value().as_list();
  auto i=static_cast<std::size_t>(cursor.get());
  if(i>=rows.size()) {return;}
  auto row=rows.at(i).as_indexed_view();
  const auto when=row.at(0).checked_as<DateTime>();
  if(when>now) {sched.schedule(when);return;}
  out.apply(row.at(1));cursor.set(static_cast<Int>(++i));
  if(i<rows.size()) {sched.schedule(rows.at(i).as_indexed_view().at(0).checked_as<DateTime>());}
 }
};
struct DeltaPass {
 static constexpr auto name="ordinary_sequence_delta_pass";
 static void eval(In<"ts",TS<Int>> ts,Out<TS<Int>> out) {out.apply(ts.delta_value());}
};
struct TimedGraph {
 static Port<TS<Int>> compose(Wiring &w,Scalar<"data",Value> data) {
  return wire<DeltaPass>(w,wire<TimedSource>(w,data.value()));
 }
};
int main() {
 try {
  std::cout << "{\"source_sha256\":\"" << SOURCE_SHA256 << "\",\"observed\":{";
  Value original=list({1,2});Value copied=original;Value cloned=original.clone();
  auto owner_view=original.view();auto old_list_view=owner_view.as_list();
  original.as_list().begin_mutation().set(0,Value{Int{99}}.view());append(original.view(),3);
  field("native_value_copy",copied.view());field("native_value_clone",cloned.view());
  field("native_borrowed_owner_after_mutation",owner_view);
  // Container view is read before replacement/destruction; no stale element pointer is dereferenced.
  textfield("native_existing_list_view_size",std::to_string(old_list_view.size()));
  Value nested=list({1,2});auto &r=TypeRegistry::instance();
  auto nested_binding=ValuePlanFactory::instance().type_for(r.mutable_list(nested.schema()));
  Value outer{nested_binding};outer.as_list().begin_mutation().push_back(nested.view());
  const auto *tuple_schema=r.tuple({scalar_descriptor<DateTime>::value_meta(),nested.schema()});
  BundleBuilder tuple{ValuePlanFactory::instance().type_for(tuple_schema)};
  tuple.set(0,Value{MIN_ST});tuple.set(1,nested.view());Value timed_entry=tuple.build();
  append(nested.view(),9);
  field("native_push_nested_copy",outer.view());
  field("native_tuple_nested_copy",timed_entry.as_indexed_view().at(1));
  Value store_source=list({1,2});GlobalState gs;gs.view().set("ordinary",store_source);
  append(store_source.view(),9);field("native_global_set_copy",gs.view().get("ordinary"));
  Value retained{gs.view().get("ordinary")};Value second_copy=retained.clone();
  append(gs.view().get("ordinary"),3);
  field("native_global_borrowed_mutation",gs.view().get("ordinary"));
  field("native_global_get_owned_copy",retained.view());
  gs.view().set("ordinary",list({7}));
  field("native_global_owned_after_replace",retained.view());
  field("native_global_replacement",gs.view().get("ordinary"));
  field("native_global_separate_clone",second_copy.view());
  ListBuilder immutable{ValuePlanFactory::instance().type_for(scalar_descriptor<Int>::value_meta())};
  immutable.push_back(Value{Int{1}}.view());Value frozen=immutable.build();
  try {append(frozen.view(),2);textfield("immutable_mutation","accepted");}
  catch(const std::exception &) {textfield("immutable_mutation","rejected");}
  const auto *event_schema=r.tuple({scalar_descriptor<DateTime>::value_meta(),scalar_descriptor<Int>::value_meta()});
  const auto event_binding=ValuePlanFactory::instance().type_for(event_schema);
  ListBuilder events{event_binding};
  const Int payloads[]={0,-7,-7};
  for(Int i=0;i<3;++i) {
   BundleBuilder event{event_binding};event.set(0,Value{MIN_ST+TimeDelta{3*i}});event.set(1,Value{payloads[i]});events.push_back(event.build());
  }
  auto recorded=testing::eval_node<TimedGraph>(arg<"data">(events.build()));
  if(!first) {std::cout << ',';}
  std::cout << "\"native_timed_direct_list\":[";
  for(std::size_t i=0;i<recorded.size();++i) {
   if(i) {std::cout << ',';}
   if(recorded[i]) {std::cout << *recorded[i];} else {std::cout << "null";}
  }
  std::cout << "]},\"libraries\":[";
 } catch(const std::exception &e) {std::cerr << e.what() << '\n';return 1;}
 bool first_library=true;
 for(const auto &p:loaded_libraries()) {
  if(std::filesystem::path(p).filename().string().find("hgraph")==std::string::npos) {continue;}
  if(!first_library) {std::cout << ',';} first_library=false;std::cout << std::quoted(p);
 }
 std::cout << "]}\n";
}
