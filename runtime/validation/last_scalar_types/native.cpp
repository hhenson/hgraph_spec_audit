#include <hgraph/lib/testing/eval_node.h>
#include <hgraph/types/static_node.h>
#include <hgraph/types/value/any_ops.h>
#include "../fixed/native_loaded_libraries.h"
#include <compare>
#include <iomanip>
#include <iostream>
#include <optional>
#include <string>
#include <vector>
using namespace hgraph;
struct Token { std::string text; auto operator<=>(const Token &) const = default; };
struct OtherToken { std::string text; bool operator==(const OtherToken &) const = default; };
struct NoOps { Int value; };
std::ostream &operator<<(std::ostream &out, const Token &v) { return out << v.text; }
std::ostream &operator<<(std::ostream &out, const OtherToken &v) { return out << v.text; }
std::ostream &operator<<(std::ostream &out, const NoOps &v) { return out << v.value; }
namespace std { template<> struct hash<Token> { size_t operator()(const Token &v) const { return hash<string>{}(v.text); } }; }
namespace hgraph {
template<> struct scalar_descriptor<Token> {
    static constexpr bool is_concrete() noexcept { return true; }
    static const ValueTypeMetaData *value_meta() { return TypeRegistry::instance().register_scalar<Token>("audit.Token"); }
};
}
Value boxed() { return Value{any_type()}; }
Value boxed(const Value &inner) { Value result=boxed(); result.as_any().begin_mutation().set(inner.view()); return result; }
std::string describe(const ValueView &v) {
    if(!v.valid()) return "empty";
    if(v.schema()==scalar_descriptor<Int>::value_meta()) return "i64:"+std::to_string(v.checked_as<Int>());
    if(v.schema()==scalar_descriptor<Bool>::value_meta()) return v.checked_as<Bool>()?"bool:true":"bool:false";
    if(v.schema()==scalar_descriptor<Bytes>::value_meta()) return "bytes:"+std::to_string(v.checked_as<Bytes>().data.size());
    if(v.schema()==scalar_descriptor<Str>::value_meta()) return "str:"+v.checked_as<Str>();
    return "native:"+v.checked_as<Token>().text;
}
struct AnySource {
    static constexpr auto name="any_source";
    static void eval(In<"step",TS<Int>> step, Out<TS<AnyValue>> out) {
        switch(step.value()) {
        case 1: out.apply(boxed().view()); break;
        case 2: out.set(Value{Int{0}}); break;
        case 3: out.set(Value{Bool{false}}); break;
        case 4: out.set(Value{Bytes{}}); break;
        case 5: out.set(Value{Str{}}); break;
        case 6: case 7: out.set(Value{Token{"one"}}); break;
        }
    }
};
struct AnyPass {
    static constexpr auto name="any_pass";
    static void eval(In<"value",TS<AnyValue>> value, Out<TS<AnyValue>> out) { out.apply(value.delta_value()); }
};
struct AnyObserve {
    static constexpr auto name="any_observe";
    static void eval(In<"value",TS<AnyValue>> value, Out<TS<Str>> out) { out.set(describe(value.contained_value())); }
};
struct AnyGraph {
    static Port<TS<Str>> compose(Wiring &w, Port<TS<Int>> step) { return wire<AnyObserve>(w,wire<AnyPass>(w,wire<AnySource>(w,step))); }
};
struct NativeSource {
    static constexpr auto name="native_source";
    static void eval(In<"step",TS<Int>> step, Out<TS<Token>> out) { out.set(Token{step.value()==1?"one":"two"}); }
};
struct NativePass {
    static constexpr auto name="native_pass";
    static void eval(In<"value",TS<Token>> value, Out<TS<Token>> out) { out.set(value.value()); }
};
struct NativeObserve {
    static constexpr auto name="native_observe";
    static void eval(In<"value",TS<Token>> value, Out<TS<Str>> out) { out.set(value.value().text); }
};
struct NativeGraph {
    static Port<TS<Str>> compose(Wiring &w, Port<TS<Int>> step) { return wire<NativeObserve>(w,wire<NativePass>(w,wire<NativeSource>(w,step))); }
};
int main() {
    try {
        auto &r=TypeRegistry::instance();
        const auto *token=r.register_scalar<Token>("audit.Token");
        const auto *other=r.register_scalar<OtherToken>("audit.OtherToken");
        r.register_scalar<NoOps>("audit.NoOps");
        Value one{Token{"one"}}, same{Token{"one"}}, two{Token{"two"}};
        Value empty=boxed(), another=boxed(), a=boxed(one), b=boxed(same);
        Value original=boxed(one), copy=original;
        original.as_any().begin_mutation().set(two.view());
        Value retained=one; one.begin_mutation().as<Token>().text="changed";
        std::cout << "{\"source_sha256\":" << std::quoted(SOURCE_SHA256) << ",\"observed\":{";
        bool first=true;
        auto emit=[&](const char *name,bool value) { if(!first) std::cout << ','; first=false; std::cout << std::quoted(name) << ':' << (value?"true":"false"); };
        emit("any_empty_present",empty.has_value() && !empty.as_any().has_value());
        emit("any_empty_equal",empty.equals(another));
        emit("any_empty_before_present",empty.compare(a)==std::partial_ordering::less);
        emit("any_equal_hash",a.equals(b) && a.hash()==b.hash());
        Value numeric=boxed(Value{Int{0}}), boolean=boxed(Value{Bool{false}});
        emit("any_distinct_type_unequal",!numeric.equals(boolean));
        emit("any_distinct_type_unordered",numeric.compare(boolean)==std::partial_ordering::unordered);
        Value flattened=boxed(a);
        emit("any_flattens",!flattened.as_any().get().is_any() && flattened.equals(a));
        Value assigned=boxed(); auto destination=assigned.begin_mutation();
        assigned.binding().ops_ref().copy_assign_from(assigned.binding(),destination.mutable_data(),a.binding(),a.view().data());
        emit("any_erased_assignment_flattens",!assigned.as_any().get().is_any() && assigned.equals(a));
        emit("any_retained_independently",copy.as_any().get().checked_as<Token>().text=="one");
        emit("native_nominal_identity",token!=other && !retained.equals(Value{OtherToken{"one"}}));
        emit("native_retained_independently",retained.view().checked_as<Token>().text=="one");
        emit("native_equal_hash",retained.equals(same) && retained.hash()==same.hash());
        emit("native_order",retained.compare(two)==std::partial_ordering::less);
        Value no=boxed(Value{NoOps{1}}), no2=boxed(Value{NoOps{1}});
        auto capability=[&](const char *name,auto operation) {
            std::cout << ',' << std::quoted(name) << ':';
            try { std::cout << std::quoted(operation()); }
            catch(const std::exception &e) { std::cout << "{\"error\":" << std::quoted(e.what()) << '}'; }
        };
        capability("any_missing_equality",[&]() { return no.equals(no2)?std::string("true"):std::string("false"); });
        capability("any_missing_hash",[&]() { return std::to_string(no.hash()); });
        capability("any_missing_order",[&]() { return no.compare(no2)==std::partial_ordering::unordered?std::string("unordered"):std::string("ordered"); });
        std::cout << "},\"graphs\":{";
        auto rows=[](auto values) { std::cout << '['; bool first=true; for(const auto &v:values) { if(!first) std::cout << ','; first=false; if(v) std::cout << std::quoted(*v); else std::cout << "null"; } std::cout << ']'; };
        std::cout << "\"any\":"; rows(testing::eval_node<AnyGraph>(std::vector<std::optional<Int>>{1,2,3,4,5,6,7,std::nullopt}));
        std::cout << ",\"native\":"; rows(testing::eval_node<NativeGraph>(std::vector<std::optional<Int>>{1,1,std::nullopt,2,std::nullopt}));
        std::cout << "},\"libraries\":[";
        bool first_library=true;
        for(const auto &path:loaded_libraries()) {
            if(std::filesystem::path(path).filename().string().find("hgraph")==std::string::npos) continue;
            if(!first_library) std::cout << ',';
            first_library=false; std::cout << std::quoted(path);
        }
        std::cout << "]}\n";
    } catch(const std::exception &e) { std::cerr << e.what() << '\n'; return 1; }
}
