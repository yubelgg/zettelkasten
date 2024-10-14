---
id: struct-records
aliases:
  - struct and records
tags: []
---

# Structures and Records

A **record** is a package that contains the possibility of variables with different types.
Each variabe is called a **field** of the record.

- java has no distinguished notion of `struct`, its all classes

An example of a struct in **C**:

- to refer to a given field of the record, use the "dot" notation

```c
struct dmy {
   int day;
   int month;
   int year;
};
struct dmy x;  // a record x of the dmy kind
struct dmy y;  // a record y of the dmy kind

x.day = 31;
x.month = 12;
x.year = 2020;

// nested structs allowed
struct ore {
    char name[30];
    struct {
        char name[2];
        int atomic_number;
        double atomic_weight;
        _Bool metallic;
    } element_yielded;
};
```

### Memory layout

The fields are keep in adjacent locations in memory.
In its symbol table, the compiler keeps track of the offset of each field of each record type.
When it needs to access a field, compiler will generate load or store instr. with displacement addressing.
For a local object, the base register is typically the frame pointer; the displacement is then
the sum of the record’s offset from the register and the field’s offset within the record.

![[structs-cpp-java.png]]

Value models of variables in C:

```c
struct S s1;
struct S s2;
s1.n.j = 0;
s2 = s1;
s2.n.j = 7;
printf("%d\n", s1.n.j); /* prints 0 */
```

Reference models of variables in java:

```java
S s1 = new S();
s1.n = new T(); // fields initialized to 0
S s2 = s1;
s2.n.j = 7;     // alias for s1.n.j
System.out.println(s1.n.j);
```
