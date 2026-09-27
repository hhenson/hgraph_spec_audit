
## Example 1

```hgl
native fn known(value: schema) -> bool {
    cpp(const hgraph::TSValueTypeMetaData *value) {
        return value != nullptr;
    }
}

for index, value_schema in items(schemas(values)) {
    if known(value_schema) { ... }
}
```

