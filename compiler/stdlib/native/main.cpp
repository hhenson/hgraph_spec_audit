#include <nodes.h>
#include <operators.h>
#include <standard.h>
#include <hgraph/lib/testing/eval_node.h>

#include <iostream>
#include <optional>
#include <utility>
#include <vector>

using ticks = std::vector<std::optional<hgraph::Int>>;

template <class Graph, class... Inputs>
bool check(const char *json_name, const ticks &expected, Inputs &&...inputs) {
    const auto actual = hgraph::testing::eval_node<Graph>(std::forward<Inputs>(inputs)...);
    std::cout << "{\"name\":" << json_name << ",\"ticks\":[";
    bool first = true;
    for (const auto &value : actual) {
        if (!first) std::cout << ',';
        first = false;
        if (value) std::cout << *value;
        else std::cout << "null";
    }
    const bool matches = actual == expected;
    std::cout << "],\"matches\":" << (matches ? "true" : "false") << "}\n";
    return matches;
}

int main() {
    hgraph_::operators_::register_operators();
    hgraph_::std_::register_operators();
    conformance::stdlib::register_operators();
#include "cases.inc"
}
