#include <iostream>
int seed = 7;
int choose(int, int second = seed) { return second; }
int unevaluated(int first, int second = sizeof(first)) { return second; }
template<int N> int specialized(int value = N) { return value; }
struct Pair { int first = 7; int second = first; };
int count = 0;
int bump() { return ++count; }
int omitted(int value = bump()) { return value; }
int main() {
    seed = 9;
    Pair pair{99};
    int a = omitted(), b = omitted();
    std::cout << std::boolalpha
        << "{\"enclosing_name\":[" << choose(99) << ',' << choose(99, 5)
        << "],\"unevaluated_parameter\":" << (unevaluated(99) == sizeof(int))
        << ",\"template_parameter\":[" << specialized<7>() << ',' << specialized<9>()
        << "],\"field_reference\":[" << pair.first << ',' << pair.second
        << "],\"evaluation_phase\":[" << a << ',' << b << ',' << count << "]}\n";
}
