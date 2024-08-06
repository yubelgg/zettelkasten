---
id: binding-time
aliases: []
tags: []
---

# Binding Time

A **binding** is the associating of a name and the thing that it binds to.

- static binding occurs before runtime and remains unchanged.
- dynamic binding occurs during execution and/or change during the program.

A **binding time** is the time the binding is created or when it was implemented.

**Different Times of binding**

1. Language design time:

   - the set of fundamental (primative) types
   - the available constructors
   - other aspects of language semantics

2. Language implementation time:
   examples can be

   - the precision of numbers
   - the coupling of I/O to the operation system's notion of files
   - the size of heaps and stacks

3. Program writing time:
   based on the programmer

   - algorithms
   - data structures
   - names

4. Compile time:

   - compilers can choose high-level constructs to machine code
   - even the layout of statically defined data in memory

5. Link time:

   - compilers support **separate compilation**, different modules will compile at different times
   - based on the availability of library of standard [[subroutines]]

6. Run time:
   - covers the entire span from the beginning to the end of a execution

Compiler based language implementation tend to be more efficent than interpreter
based since they make decisions ealier.

In general earlier bindings are associated with better efficency and later bindings
are associated with greater flexibility.
