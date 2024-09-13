---
id: oop
aliases: []
tags: []
---

# Object oriented programming

What is OOP?
It is a programming model that is used to organize the design around data, and objects.
Where each object contains unique attributes and behavior.

**Structure of OOP**
**Classes**: user-defined data types that act as blueprints for objects, attributes, and methods.
**Objects**: instances of a class with specifically defined data.
**Methods**: functions that objects can perform and describe the behavior of an object.
**Attributes**: states or information of an object.
![[oop.png]]

## Main Princples

4 Pillars of OOP

**Encapsulation**: all important information is contained inside an object, only selected
inforomation is exposed (public and private). Other objects won't have access and won't be
able to make changes to it.

**Abstraction**: provides only essential information, which hides the implemenation or details.
Like you know stepping on the gas makes you faster but don't know the mechanics behind it.

**Inheritance**: new classes can reuse code from an existing class by inheriting it's porperties.

> [!example]- Inheritance demo
>
> ```cpp
> #include <iostream>
> using namespace std;
>
> class A {
>     int a, b;
>
> public:
>     void add(int x, int y) {
>         a = x;
>         b = y;
>         cout << "addition of a+b is:" << (a + b) << endl;
>     }
> };
>
> class B : public A {
> public:
>     void print(int x, int y) {
>         add(x, y);
>     }
> };
>
> int main() {
>     B b1;
>     b1.print(5, 6);
>     return 0;
> }
> ```

**Polymorphism**: control to use which [[subroutines|method or functions]] to apply (overloading).

> [!example]- Polymorphism demo
>
> ```cpp
> #include "iostream"
> using namespace std;
>
> class A {
>     int a, b, c;
>
> public:
>     void add(int x, int y) {
>         a = x;
>         b = y;
>         cout << "addition of a+b is:" << (a + b) << endl;
>     }
>
>     void add(int x, int y, int z) {
>         a = x;
>         b = y;
>         c = z;
>         cout << "addition of a+b+c is:" << (a + b + c) << endl;
>     }
>
>     virtual void print() {
>         cout << "Class A's method is running" << endl;
>     }
> };
>
> class B : public A {
> public:
>     void print() {
>         cout << "Class B's method is running" << endl;
>     }
> };
>
> int main() {
>     A a1;
>
>     // method overloading (Compile-time polymorphism)
>     a1.add(6, 5);
>
>     // method overloading (Compile-time polymorphism)
>     a1.add(1, 2, 3);
>
>     B b1;
>     // Method overriding (Run-time polymorphism)
>     b1.print();
> }
> ```
>
> output:
>
> ```
> addition of a+b is:11
> addition of a+b+c is:6
> Class B's method is running
> ```
