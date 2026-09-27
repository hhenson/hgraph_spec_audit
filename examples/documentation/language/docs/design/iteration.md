
## Example 1

```cpp
#include <hgraph/lib/std/std_operators.h>
#include <hgraph/types/graph_wiring.h>
#include <hgraph/types/subgraph_wiring.h>

struct ObserveElements
{
    static constexpr auto name = "observe_elements";

    static void compose(hgraph::Wiring &w,
                        hgraph::Port<hgraph::TSL<hgraph::TS<hgraph::Float>, 3>> samples)
    {
        for (std::size_t index = 0; index < 3; ++index) {
            hgraph::wire<hgraph::stdlib::null_sink>(w, hgraph::tsl_element(samples, index));
        }
    }
};
```


## Example 2

```cpp
#include <hgraph/types/static_node.h>

struct CountAddedElements
{
    static constexpr auto name = "count_added_elements";

    static void eval(hgraph::In<"symbols", hgraph::TSS<hgraph::Str>> symbols,
                     hgraph::Out<hgraph::TS<hgraph::Int>> out)
    {
        if (symbols.modified() && symbols.valid()) {
            hgraph::Int count = 0;
            for (const auto &symbol : symbols.added()) {
                (void)symbol;
                ++count;
            }
            out.set(count);
        }
    }
};
```

