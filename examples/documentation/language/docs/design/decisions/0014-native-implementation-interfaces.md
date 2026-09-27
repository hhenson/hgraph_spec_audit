
## Example 1

```cpp
#include <native.h> // Generated from native.hgl.

struct Implementation {
    static hgraph::Int bit_and(hgraph::Int lhs, hgraph::Int rhs) noexcept {
        return lhs & rhs;
    }
};

inline constexpr auto native = example::native::native_interface::bind<Implementation>();
```


## Example 3

```cpp
static void accumulate(const Input<Int>& value, Output<Int>& out, Logger& logger);
static String describe(Int value, Logger& logger);
```

