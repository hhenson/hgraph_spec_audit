#include <hgraph/lib/testing/eval_node.h>
#include <hgraph/types/static_node.h>
#include <hgraph/types/value/json_codec.h>
#include "../fixed/native_loaded_libraries.h"
#include <iomanip>
#include <iostream>
#include <optional>
using namespace hgraph;
template<int S> using Child = std::conditional_t<S == 0, TS<Int>,
    std::conditional_t<S == 1, TS<Bool>, std::conditional_t<S == 2, TSL<TS<Int>, 2>, TSD<Int, TS<Int>>>>>;
template<int S> using Shape = UnNamedTSB<Field<"sibling", TS<Int>>, Field<"child", Child<S>>>;
template<int S, bool Present, bool Boolean = true> struct Source {
    static constexpr auto name = "unset_read_source";
    static void eval(In<"step", TS<Int>> /*step*/, Out<Shape<S>> out) {
        auto fields = out.base().as_bundle();
        auto sibling = fields.at(0);
        Out<TS<Int>>{std::move(sibling), out.evaluation_time()}.set(1);
        if constexpr(Present) {
            auto child = fields.at(1);
            if constexpr(S == 0) Out<Child<S>>{std::move(child), out.evaluation_time()}.set(Int{4});
            else if constexpr(S == 1) Out<Child<S>>{std::move(child), out.evaluation_time()}.set(Boolean);
            else if constexpr(S == 2) {
                auto list = child.as_list();
                auto first = list.at(0);
                auto second = list.at(1);
                Out<TS<Int>>{std::move(first), out.evaluation_time()}.set(4);
                Out<TS<Int>>{std::move(second), out.evaluation_time()}.set(5);
            } else Out<Child<S>>{std::move(child), out.evaluation_time()}.set(7, Int{4});
        }
    }
};
template<int S> struct Read {
    static constexpr auto name = "retained_required_read";
    static void eval(In<"step", TS<Int>> /*step*/,
                     In<"source", Shape<S>, InputValidity::Unchecked, InputActivity::Passive> source,
                     Out<TS<Str>> out) {
        Value retained{source.base().value()};
        auto held = retained.view();
        auto fields = held.as_indexed_view();
        auto child = fields.at(1);
        auto inputs = source.base().as_bundle();
        std::string text = "{\"source_child_valid\":" + std::string(inputs.at(1).valid() ? "true" : "false") +
            ",\"retained_child_valid\":" + (child.valid() ? "true" : "false");
        try {
            std::string result;
            if constexpr(S == 0) result = std::to_string(child.checked_as<Int>() + 1);
            else if constexpr(S == 1) result = child.checked_as<Bool>() ? "1" : "0";
            else if constexpr(S == 2) result = std::to_string(child.as_list().size());
            else {
                result = "["; bool first = true;
                for(const auto &[key, value] : child.as_map().items()) {
                    if(!first) result += ',';
                    first = false;
                    result += "[" + to_json_string(key) + "," + to_json_string(value) + "]";
                }
                result += ']';
            }
            text += ",\"outcome\":\"value\",\"result\":" + result;
        } catch(const std::exception &e) {
            std::ostringstream message; message << std::quoted(e.what());
            text += ",\"outcome\":\"failure\",\"error\":" + message.str();
        }
        out.set(text + '}');
    }
};
template<int S, bool Present, bool Boolean = true> struct Graph {
    static Port<TS<Str>> compose(Wiring &w, Port<TS<Int>> step) {
        return wire<Read<S>>(w, step, wire<Source<S, Present, Boolean>>(w, step));
    }
};
template<int S, bool Present, bool Boolean = true> void run(const char *name) {
    const auto result = testing::eval_node<Graph<S, Present, Boolean>>(std::vector<std::optional<Int>>{1});
    std::cout << std::quoted(name) << ':';
    if(result.size() == 1 && result[0]) std::cout << *result[0]; else std::cout << "null";
}
int main() {
    std::cout << "{\"observations\":{";
    run<0,false>("scalar_unset"); std::cout << ','; run<0,true>("scalar_present"); std::cout << ',';
    run<1,false>("bool_unset"); std::cout << ','; run<1,true>("bool_present"); std::cout << ',';
    run<1,true,false>("bool_false"); std::cout << ',';
    run<2,false>("list_unset"); std::cout << ','; run<2,true>("list_present"); std::cout << ',';
    run<3,false>("map_unset"); std::cout << ','; run<3,true>("map_present");
    std::cout << "},\"libraries\":["; bool first=true;
    for(const auto &path : loaded_libraries()) {
        if(std::filesystem::path(path).filename().string().find("hgraph") == std::string::npos) continue;
        if(!first) std::cout << ',';
        first=false; std::cout << std::quoted(path);
    }
    std::cout << "]}\n";
}
