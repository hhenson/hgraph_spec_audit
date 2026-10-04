#include <hgraph/types/static_node.h>
#include <hgraph/runtime/global_state.h>
#include <hgraph/types/value/value_builder.h>
#include "../fixed/native_loaded_libraries.h"
#include <iomanip>
#include <iostream>
using namespace hgraph;

bool retained(Value original, const Value &replacement) {
    Value expected=original.clone();
    Value recording;
    {
        auto &registry=TypeRegistry::instance();
        auto event_type=ValuePlanFactory::instance().type_for(registry.tuple({scalar_descriptor<DateTime>::value_meta(),original.schema()}));
        BundleBuilder event{event_type};
        event.set(0,Value{MIN_ST});
        event.set(1,original.view());
        Value item=event.build();
        Value rows{ValuePlanFactory::instance().type_for(registry.mutable_list(item.schema()))};
        rows.as_list().begin_mutation().push_back(item.view());
        GlobalState state;
        state.view().set("recording",rows);
        recording=Value{state.view().get("recording")};
        original=replacement;
        BundleBuilder changed{event_type};
        changed.set(0,Value{MIN_ST+MIN_TD});
        changed.set(1,replacement.view());
        item=changed.build();
        rows.as_list().begin_mutation().set(0,item.view());
        state.view().set("recording",rows);
    }
    auto captured=recording.as_list().at(0).as_indexed_view();
    return recording.as_list().size()==1 && captured.at(0).checked_as<DateTime>()==MIN_ST && expected.equals(captured.at(1)) && !replacement.equals(captured.at(1));
}
int main() {
    try {
        using Quote=UnNamedTSB<Field<"bid",TS<Int>>,Field<"ask",TS<Int>>>;
        std::cout << "{\"source_sha256\":\"" << SOURCE_SHA256 << "\",\"observed\":{";
        bool first=true;
        auto emit=[&](const char *name,Value before,Value after) {
            if(!first) std::cout << ',';
            first=false;
            std::cout << std::quoted(name) << ':' << (retained(std::move(before),after)?"true":"false");
        };
        emit("set_i64",set_delta<Int>({1,2},{}),set_delta<Int>({}, {1}));
        emit("fixed_list",list_delta<TS<Int>>({{0,10},{2,30}}),list_delta<TS<Int>>({{0,11}}));
        emit("named_bundle",tsb_delta<Quote>(Int{10},Int{20}),tsb_delta<Quote>(Int{11},std::nullopt));
        emit("map",dict_delta<Int,TS<Int>>({{1,10},{2,20}}),dict_delta<Int,TS<Int>>({{1,11}}));
        emit("nested_map",dict_delta<Int,TSD<Int,TS<Int>>>({{7,dict_delta<Int,TS<Int>>({{1,10},{2,20}})}}),dict_delta<Int,TSD<Int,TS<Int>>>({{7,dict_delta<Int,TS<Int>>({{1,11}})}}));
        emit("list_of_maps",list_delta<TSD<Int,TS<Int>>>({{0,dict_delta<Int,TS<Int>>({{1,10},{2,20}})}}),list_delta<TSD<Int,TS<Int>>>({{0,dict_delta<Int,TS<Int>>({{1,11}})}}));
        std::cout << "},\"libraries\":[";
        bool first_library=true;
        for(const auto &path:loaded_libraries()) {
            if(std::filesystem::path(path).filename().string().find("hgraph")==std::string::npos) continue;
            if(!first_library) std::cout << ',';
            first_library=false;
            std::cout << std::quoted(path);
        }
        std::cout << "]}\n";
    } catch(const std::exception &error) {std::cerr << error.what() << '\n';return 1;}
}
