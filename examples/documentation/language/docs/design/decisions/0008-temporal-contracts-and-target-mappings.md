
## Example 1

```cpp
double scale(double value, double factor) {
    return value * factor;
}

struct scaled {
    static void eval(hgraph::In<"value", hgraph::TS<double>> value,
                     hgraph::Scalar<"factor", double> factor,
                     hgraph::Out<hgraph::TS<double>> out) {
        out.set(scale(value.value(), factor.value()));
    }
};
```


## Example 2

```hgl
type SomeType {
    cpp { some::Type }
}
```

