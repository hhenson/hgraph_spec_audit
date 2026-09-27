
## Example 1

```cpp
struct ImportedStructField
{
    std::string  name{};
    ImportedType type{};
    bool         optional{false};
    bool         recursive{false};   ///< ADR 0012 edge; target named by identity
};

struct ImportedStruct
{
    std::string                      module_identity{};
    std::string                      name{};
    std::string                      identity{};       ///< m.Quote
    bool                             abstract{false};
    std::vector<ImportedGeneric>     generics{};
    std::vector<ImportedStructField> fields{};
    std::vector<ImportedType>        parents{};         ///< Symbol, by identity
    std::vector<std::string>         public_headers{};  ///< the exporter's generated header
    std::string                      descriptor_fingerprint{};
    std::string                      support_error{};
};
```

