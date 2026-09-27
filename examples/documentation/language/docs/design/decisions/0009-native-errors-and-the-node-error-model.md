
## Example 101

```hgl
   native fn power(lhs: i64, rhs: i64) -> i64 throws {
       cpp(const hgraph::Int &lhs, const hgraph::Int &rhs) {
           return hgraph::stdlib::scalar_pow<hgraph::Int>::apply(lhs, rhs);
       }
   }

```
