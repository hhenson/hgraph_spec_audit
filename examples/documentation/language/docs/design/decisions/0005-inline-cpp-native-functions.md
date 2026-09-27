
## Example 1

```hgl
cpp include <hgraph/types/time_series/ts_input/list_view.h>

native fn len<T, const size: i64>(value: list<T, size>) -> i64 {
    cpp(const hgraph::TSLInputView &value) {
        return static_cast<hgraph::Int>(value.size());
    }
}
```

