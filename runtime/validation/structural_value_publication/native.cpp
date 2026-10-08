#include <hgraph/lib/testing/eval_node.h>
#include <hgraph/types/static_node.h>
#include <hgraph/types/value/json_codec.h>
#include "../fixed/native_loaded_libraries.h"
#include <iomanip>
#include <iostream>
#include <optional>
using namespace hgraph;
using Pair = UnNamedTSB<Field<"left", TS<Int>>, Field<"right", TS<Int>>>;
template<int S> using Shape = std::conditional_t<S == 0, Pair,
    std::conditional_t<S == 1, TSL<TS<Int>, 2>, TSD<Int, TS<Int>>>>;

std::vector<std::string> retentions;
std::string json_value(const ValueView &v) {
    if(!v.valid()) return "null";
    if(v.is_bundle() || v.is_list() || v.is_tuple()) {
        const auto items = v.as_indexed_view();
        std::string text = v.is_bundle() ? "{" : "[";
        for(std::size_t i = 0; i < items.size(); ++i) {
            if(i) text += ',';
            if(v.is_bundle()) text += '"' + std::string(v.schema()->fields[i].name) + "\":";
            text += json_value(items.at(i));
        }
        return text + (v.is_bundle() ? "}" : "]");
    }
    if(v.is_map()) {
        std::string text = "{";
        bool first = true;
        for(const auto &[key, value] : v.as_map().items()) {
            if(!first) text += ',';
            first = false;
            text += '"' + to_json_string(key) + "\":" + json_value(value);
        }
        return text + '}';
    }
    return to_json_string(v);
}
template<int S, typename View> auto child(const View &v, std::size_t index) {
    if constexpr(S == 0) { auto children = v.as_bundle(); return children.at(index); }
    else { auto children = v.as_list(); return children.at(index); }
}
std::string leaf(const TSInputView &v) {
    return "{\"valid\":" + std::string(v.valid() ? "true" : "false") +
        ",\"value\":" + (v.valid() ? std::to_string(v.value().checked_as<Int>()) : "null") + '}';
}
template<int S, typename Input> std::string state(const Input &v) {
    std::string out = "{\"valid\":" + std::string(v.valid() ? "true" : "false") +
        ",\"all_valid\":" + (v.all_valid() ? "true" : "false") +
        ",\"modified\":" + (v.modified() ? "true" : "false") + ",\"children\":{";
    if constexpr(S < 2) {
        for(std::size_t i = 0; i < 2; ++i) {
            if(i) out += ',';
            out += '"' + std::string(S == 0 ? (i ? "right" : "left") : (i ? "1" : "0")) + "\":";
            out += leaf(child<S>(v.base(), i));
        }
    } else {
        bool first = true;
        for(Int key : {7, 8}) if(v.contains(key)) {
            if(!first) out += ',';
            first = false;
            out += '"' + std::to_string(key) + "\":" + leaf(v[key].base());
        }
    }
    return out + "}}";
}
template<int S, bool Partial> struct Source {
    static constexpr auto name = "structural_value_source";
    static void eval(In<"step", TS<Int>> step, Out<Shape<S>> out) {
        const auto tick = step.value();
        if constexpr(S < 2) {
            if(tick == 1 || (Partial && tick == 2)) {
                auto left = child<S>(out.base(), 0);
                Out<TS<Int>>{std::move(left), out.evaluation_time()}.set(Partial ? 30 : 10);
                if constexpr(!Partial) {
                    auto right = child<S>(out.base(), 1);
                    Out<TS<Int>>{std::move(right), out.evaluation_time()}.set(20);
                }
            }
        } else {
            if(tick == 1) { out.set(7, Int{10}); out.set(8, Int{20}); }
            if(tick == 2) {
                if constexpr(S == 2) static_cast<void>(out.erase(8));
                else static_cast<void>(out[8].begin_mutation(out.evaluation_time()).invalidate());
            }
        }
    }
};
template<int S> struct Copy {
    static constexpr auto name = "structural_owned_value_copy";
    static void eval(In<"step", TS<Int>> step,
                     In<"a", Shape<S>, InputValidity::Unchecked, InputActivity::Passive> a,
                     In<"b", Shape<S>, InputValidity::Unchecked, InputActivity::Passive> b,
                     Out<Shape<S>> out) {
        const auto source = (S >= 2 || step.value() == 1) ? a.base().value() : b.base().value();
        const auto source_value = json_value(source);
        Value retained{source};
        retentions.push_back("{\"step\":" + std::to_string(step.value()) +
            ",\"source_value\":" + source_value + ",\"retained_value\":" + json_value(retained.view()) + '}');
        auto mutation = out.base().begin_mutation(out.evaluation_time());
        static_cast<void>(mutation.copy_value_from(retained.view()));
    }
};
template<int S> struct Observe {
    static constexpr auto name = "structural_state_observer";
    static void eval(In<"step", TS<Int>> step,
                     In<"a", Shape<S>, InputValidity::Unchecked, InputActivity::Passive> a,
                     In<"b", Shape<S>, InputValidity::Unchecked, InputActivity::Passive> b,
                     In<"copied", Shape<S>, InputValidity::Unchecked, InputActivity::Passive> copied,
                     Out<TS<Str>> out) {
        const auto source = (S >= 2 || step.value() == 1) ? state<S>(a) : state<S>(b);
        out.set("{\"step\":" + std::to_string(step.value()) + ",\"source\":" + source +
                ",\"output\":" + state<S>(copied) + '}');
    }
};
template<int S> struct Graph {
    static Port<TS<Str>> compose(Wiring &w, Port<TS<Int>> step) {
        auto a = wire<Source<S, false>>(w, step);
        auto b = [&]() { if constexpr(S < 2) return wire<Source<S, true>>(w, step); else return a; }();
        auto copied = wire<Copy<S>>(w, step, a, b);
        return wire<Observe<S>>(w, step, a, b, copied);
    }
};
template<int S> void run(const char *name) {
    const std::vector<std::optional<Int>> steps{1, 2, 3};
    retentions.clear();
    const auto result = testing::eval_node<Graph<S>>(steps);
    std::cout << std::quoted(name) << ":{\"raw_eval_node\":[";
    bool first = true;
    for(const auto &value : result) {
        if(!first) std::cout << ',';
        first = false;
        if(value) std::cout << std::quoted(*value); else std::cout << "null";
    }
    std::cout << "],\"retentions\":[";
    first = true;
    for(const auto &row : retentions) {
        if(!first) std::cout << ',';
        first = false;
        std::cout << std::quoted(row);
    }
    std::cout << "]}";
}
int main() {
    try {
        std::cout << "{\"source_sha256\":\"" << SOURCE_SHA256 << "\",\"observed\":{";
        run<0>("struct"); std::cout << ',';
        run<1>("fixed"); std::cout << ',';
        run<2>("map_remove"); std::cout << ',';
        run<3>("map_invalid");
        std::cout << "},\"libraries\":[";
        bool first = true;
        for(const auto &path : loaded_libraries()) {
            if(std::filesystem::path(path).filename().string().find("hgraph") == std::string::npos) continue;
            if(!first) std::cout << ',';
            first = false;
            std::cout << std::quoted(path);
        }
        std::cout << "]}\n";
    } catch(const std::exception &error) { std::cerr << error.what() << '\n'; return 1; }
}
