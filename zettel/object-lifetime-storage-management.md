---
id: object-lifetime-storage-management
aliases: []
tags: []
---

# lifetimes

Several key events when to distinguish between names and objects which they refer to:

- the creation and destruction of objects
- the creation and destruction of bindings
- the deactivation and reactivations which leaves them unusable for a period
- references to variables, [[subroutines]], types, and more are all bindings

The creation and destruction of a name to object binding is a **binding's lifetime**.
The creation and destruction of an object is the **object's lifetime**.

Object lifetimes are usually one of three principals of **storage allocation**.

1. [[static-mem |static]] objects given an absolute address that remains the same throughout the execution of the program
2. [[stack-mem |stack]] objects that are allocated and deallocated in last-in, first-out order
3. [[heap-mem |heap]] objects allocated and deallocated at random times
