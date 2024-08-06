---
id: types
aliases: []
tags: []
---

# Types Purpose

Types serve several purposes in programming languages:

- types provide implicit context for many operations
- limits the set of operations that may be performed
- making it easier to read and understand, serves as documentation
- if types are know at compile time, it can be optimized for performance

## Polymorphism

Polymorphism is designed to work with multiple types.

The types must generally have certain characteristics in common, and not any other characteristics.

Two main ways:

- **Parametric Polymorphism** takes a type (or set of types) as parameters
  - known as **generics** or **templates** in cpp
  - typically appears in statically typed languages
  - implemented at compile time
- **Subtype Polymorphism** is designed to work with a specific type **T**
  - typically appears in object oriented languages
  - `(List<T>)` or `(Stack<T>)`

> [!info]+ cpp code for parametric Polymorphism
>
> ```cpp
> #include <iostream>
>
> // Template function definition
> template <typename T>
> T add(T a, T b) {
>     return a + b;
> }
>
> int main() {
>     // Explicitly specifying the type
>     std::cout << add<int>(3, 4) << std::endl;    // Outputs 7
>     std::cout << add<double>(3.5, 2.3) << std::endl; // Outputs 5.8
>     return 0;
> }
> ```
>
> ```cpp
> #include <iostream>
>
> // Template class definition
> template <typename T>
> class Pair {
> public:
>     T first, second;
>
>     Pair(T a, T b) : first(a), second(b) {}
>
>     T getMax() {
>         return (first > second) ? first : second;
>     }
> };
>
> int main() {
>     // Explicitly specifying the type
>     Pair<int> intPair(1, 2);
>     Pair<double> doublePair(1.1, 2.2);
>
>     std::cout << intPair.getMax() << std::endl;       // Outputs 2
>     std::cout << doublePair.getMax() << std::endl;    // Outputs 2.2
>
>     return 0;
> }
> ```
>
> ```cpp
> #include <iostream>
>
> // Explicit Template Instantiation
> template <typename T>
> void printValue(T value) {
>     std::cout << value << std::endl;
> }
>
> int main() {
>     printValue<int>(5);        // Explicit instantiation, prints 5
>     printValue(5);             // Implicit instantiation, type deduced as int
>     printValue<double>(3.14);  // Explicit instantiation, prints 3.14
>
>     return 0;
> }
> ```
