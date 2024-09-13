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

**Abstraction**: provides only essential information, which hides the implementation or details.
Like you know stepping on the gas makes you faster but don't know the mechanics behind it.

```cpp
// Abstract class
abstract class Animal {
  public abstract void animalSound();// Abstract method (does not have a body)
  public void sleep() {             // Regular method
    System.out.println("Zzz");
  }
}

// Subclass (inherit from Animal)
class Pig extends Animal {
  public void animalSound() {    // The body of animalSound() is provided here
    System.out.println("The pig says: wee wee");
  }
}

class Main {
  public static void main(String[] args) {
    Pig myPig = new Pig(); // Create a Pig object
    myPig.animalSound();
    myPig.sleep();
  }
}
```

**Inheritance**: new classes can reuse code from an existing class by inheriting it's porperties.

```cpp
#include <iostream>
using namespace std;

class A {
    int a, b;

public:
    void add(int x, int y) {
        a = x;
        b = y;
        cout << "addition of a+b is:" << (a + b) << endl;
    }
};

class B : public A {
public:
    void print(int x, int y) {
        add(x, y);
    }
};

int main() {
    B b1;
    b1.print(5, 6);
    return 0;
}
```

**Polymorphism**: control to use which [[subroutines|method or functions]] to apply (overloading).

```cpp
#include "iostream"
using namespace std;

class A {
    int a, b, c;

public:
    void add(int x, int y) {
        a = x;
        b = y;
        cout << "addition of a+b is:" << (a + b) << endl;
    }

    void add(int x, int y, int z) {
        a = x;
        b = y;
        c = z;
        cout << "addition of a+b+c is:" << (a + b + c) << endl;
    }

    virtual void print() {
        cout << "Class A's method is running" << endl;
    }
};

class B : public A {
public:
    void print() {
        cout << "Class B's method is running" << endl;
    }
};

int main() {
    A a1;

    // method overloading (Compile-time polymorphism)
    a1.add(6, 5);

    // method overloading (Compile-time polymorphism)
    a1.add(1, 2, 3);

    B b1;
    // Method overriding (Run-time polymorphism)
    b1.print();
}
```

output:

```
addition of a+b is:11
addition of a+b+c is:6
Class B's method is running
```

## Interfaces

Interfaces are used to achieve abstraction, it is a `abstract class`.
However interfaces methods don't have a method body, the body is provided by the
implemented class

We use interfaces since we can `implements` multiple interfaces, since java doesn't
support "multiple inheritance" (`extends`).

- interface methods are by default abstract and public
- interface attributes are by default public, static, final
- cannot be used to create objects like abstract classes

You must override all it's methods

```cpp
// Interface
interface Animal {
  public void animalSound();    // interface method (does not have a body)
  public void sleep();          // interface method (does not have a body)
}

// Pig "implements" the Animal interface
class Pig implements Animal {
  public void animalSound() {   // The body of animalSound() is provided here
    System.out.println("The pig says: wee wee");
  }
  public void sleep() {         // The body of sleep() is provided here
    System.out.println("Zzz");
  }
}

class Main {
  public static void main(String[] args) {
    Pig myPig = new Pig();      // Create a Pig object
    myPig.animalSound();
    myPig.sleep();
  }
}
```
