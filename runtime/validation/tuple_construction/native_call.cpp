// Direct std::tuple call expressions: do not pre-evaluate their arguments.
#include <iostream>
#include <stdexcept>
#include <tuple>
#include <vector>

std::vector<int> trace;
int mark(int value) { trace.push_back(value); return value; }
int fail(int value) { trace.push_back(value); throw std::runtime_error("element failed"); }
void emit_trace() {
    std::cout << '[';
    for (std::size_t i = 0; i < trace.size(); ++i) {
        if (i) std::cout << ',';
        std::cout << trace[i];
    }
    std::cout << ']';
}
int main() {
    auto value = std::tuple<int, int>(mark(2), mark(1));
    std::cout << "{\"success_trace\":";
    emit_trace();
    std::cout << ",\"value\":[" << std::get<0>(value) << ',' << std::get<1>(value) << ']';
    trace.clear();
    bool constructed = false;
    try { auto failed = std::tuple<int, int>(fail(2), mark(1)); (void)failed; constructed = true; }
    catch (const std::runtime_error&) {}
    std::cout << ",\"failure_trace\":";
    emit_trace();
    std::cout << ",\"constructed\":" << (constructed ? "true" : "false") << "}\n";
}
