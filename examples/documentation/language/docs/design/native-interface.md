
## Example 1

```hgl
cpp include <hgraph/types/time_series/ts_input/list_view.h>

native fn len<T, const size: i64>(value: list<T, size>) -> i64 {
    cpp(const hgraph::TSLInputView &value) {
        return static_cast<hgraph::Int>(value.size());
    }
}
```


## Example 2

```hgl
native fn power(lhs: i64, rhs: i64) -> i64 throws {
    cpp(const hgraph::Int &lhs, const hgraph::Int &rhs) {
        return hgraph::stdlib::scalar_pow<hgraph::Int>::apply(lhs, rhs);
    }
}
```


## Example 3

```hgl
native fn increment(value: f64) -> f64 {
    cpp(hgraph::Float value) {
        return value + 1.0;
    }
}

fn incremented(value: f64) -> f64 {
    when modified(value) && valid(value) {
        return increment(value)
    }
}
```


## Example 4

```cpp
#include <hgl/native_package.h>

int main()
{
    using namespace hgl::native;
    Package package{
        .module_identity = "acme.stats",
        .language_version = "0.1",
        .declarations = {
            Declaration{
                .identity = "acme.stats::update",
                .cpp_symbol = "acme::stats::update",
                .parameters = {
                    Parameter{.name = "previous",
                              .type = ValueType::canonical(ScalarType::F64)},
                    Parameter{.name = "value",
                              .type = ValueType::canonical(ScalarType::F64)},
                },
                .result_type = ValueType::canonical(ScalarType::F64),
                .phases = {Phase::Evaluation},
            },
        },
        .build = Build{
            .public_headers = {"acme/stats.h"},
            .cmake_packages = {"acme_stats"},
            .imported_targets = {"acme::stats"},
        },
    };
    write_descriptor(package, "acme-stats.hgl-module.json");
}
```


## Example 5

```cpp
const ValueType i64 = ValueType::canonical(ScalarType::I64);
const ValueType t = ValueType::type_parameter("T");

Declaration{
    .identity = "hgraph.native::len",
    .cpp_symbol = "hgraph::native::len",
    .generics = {
        GenericParameter{.name = "T"},
        GenericParameter{.name = "N", .is_const = true, .type = i64},
    },
    .parameters = {
        Parameter{
            .name = "value",
            .type = ValueType::list(t, "N"),
            .access = ParameterAccess::InputView,
        },
    },
    .result_type = i64,
    .phases = {Phase::Evaluation},
}
```


## Example 6

```cpp
Declaration{
    .identity = "hgraph.native::valid",
    .cpp_symbol = "hgraph::native::valid",
    .parameters = {
        Parameter{
            .name = "value",
            .type = ValueType::signal(),
            .access = ParameterAccess::InputView,
        },
    },
    .result_type = ValueType::canonical(ScalarType::Bool),
    .phases = {Phase::Evaluation},
}
```

