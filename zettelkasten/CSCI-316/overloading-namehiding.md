---
id: overloading-namehiding
aliases: []
tags: []
---

## Overloading

Using same identifier to define multiple methods that differ in input and output parameters.

Overloading functions are done within the same class.

Within the symbol table of a compiler, overloading must be handled (resolved) by arranging
for the lookup routine to return a list of possible meanings for the requested name.

```cpp
struct complex {
    double real, imaginary;
};

enum base {dec, bin, oct, hex};

int i;
complex x;

void print_num(int n) { ...
void print_num(int n, base b) { ...
void print_num(complex c) { ...

print_num(i);       // uses the first function above
print_num(i, hex);  // uses the second function above
print_num(x);       // uses the third function above
```

## Name Hiding

Actually, the name lookup that is run by C++ will stop looking for other names as soon as it
finds a single name in one of your base classes. This is because the someFunction
declaration in ChildClass actually **hides** the someFunction declaration in ParentClass – so
when a call to someFunction is made from GrandChildClass, the name lookup does not “see”
the someFunction declaration that is in the ParentClass.

```cpp
class ParentClass
{
    public:
    void someFunction(string s){ };
};

class ChildClass : public ParentClass
{
    public:
    int someFunction(int i){};
};

class GrandChildClass : public ChildClass
{
    public:
    void differentFunction()
    {
        String s;
        /*This call will result in an error:  */
        someFunction(s);
    }
};
```

A solution to the name hiding is by implementing the **using** keyword.

When we redeclare someFunction in the scope of ChildClass (with the “using” keyword), it
makes both versions of that function (from both ChildClass and GrandChildClass) visible in
just the ChildClass.

```cpp
class ParentClass
{
    public:
    void someFunction(string s){ };
};

class ChildClass : public ParentClass
{
    public:
    int someFunction(int i){};

    /*This makes the someFunction
       declaration in ParentClass visible
       here as well:
    */
    using ParentClass::someFunction;
};

class GrandChildClass : public ChildClass
{
    public:
    void differentFunction()
    {
        String s;
        /*This call will result in an error:  */
        someFunction(s);

    }
};
```

Name hiding is good since you may end up using the wrong function.
