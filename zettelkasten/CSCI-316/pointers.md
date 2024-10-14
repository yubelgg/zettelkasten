---
id: pointers
aliases: []
tags: []
---

# Pointers

Pointers are variables that store memory addresses of an object.

A raw pointer can be assigned the address of another non-pointer variable, or
it can be assigned a value of nullptr. A pointer that hasn't been assigned a
value contains random data.

A pointer can also be dereferenced to retrieve the value of the object that it
points at. The member access operator provides access to an object's members.

An advantage for pointers is memory management, since you can pass pointers to objects
instead of coping them over and over.

```cpp
int* p = nullptr;   // declare pointer and initialize it
                    // so that it doesn't store a random address
int i = 5;
p = &i;             // assign pointer to address of object
int j = *p;         // dereference p to retrieve the value at its address

MyClass* mc = new MyClass();    // allocate object on the heap
mc->print();                    // access class member
delete mc;                      // delete object (please don't forget!)
```

pointer to pointers:

```cpp
int value = 10;
int* ptr = &value;
int** ptr_to_ptr = &ptr;  // Pointer to a pointer to int

std::cout << **ptr_to_ptr;  // Outputs 10
```

```c
#include <stdio.h>

struct Person {
    char name[64];
    int age;
}

void updateStruct(struct Person *p, int age) {
    p->age = age;
}

int main(int argc, char **argv) {
    struct Person me;
    updateStruct(&me, 22);
}
```

### Smart Pointers

In modern C++ programming, the Standard Library includes smart pointers, which
are used to help ensure that programs are free of memory and resource leaks and
are exception-safe.

```cpp
void UseRawPointer()
{
    // Using a raw pointer -- not recommended.
    Song* pSong = new Song(L"Nothing on You", L"Bruno Mars");

    // Use pSong...

    // Don't forget to delete!
    delete pSong;
}

void UseSmartPointer()
{
    // Declare a smart pointer on stack and pass it the raw pointer.
    unique_ptr<Song> song2(new Song(L"Nothing on You", L"Bruno Mars"));

    // Use song2...
    wstring s = song2->duration_;
    //...

} // song2 is deleted automatically here.
```
