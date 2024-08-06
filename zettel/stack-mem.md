---
id: stack-mem
aliases: []
tags: []
---

# Stack memory

A memory allocation and deallocation using a stack data structure.

Usually used for managing local variables within functions and function management.

Each instance of a [[subroutines|subroutine]] at runtime has its own **frame** (activation record):

- frame pointer - points to a known location of the current [[subroutines|subroutine]]
- return address
- function arguments
- local variables
- temporaries - hold immediate values from calculations,
- bookeeping - contains the [[subroutines|subroutine]]'s:
  - return address
  - the reference to the stack frame called the **dynamic link**.
- local variables, temporaries, and bookeeping have a negative **offset** from the frame pointer.
- function arguments and return usually have a positive **offset**

Maintenance of the stack is the responsibility of the [[subroutines|subroutine]] **calling sequence**.

- the code executed by the user before and after the call
- the prologue (code executed at the beginning) [[subroutines|subroutine]]
- the epilogue (code executed at the end) of the [[subroutines|subroutine]]

![[stack-mem-demo.png]]

The stack grow ==downwards== towards lower addresses for most language implementations.

## Characteristics:

1. Last-in-first-out (LIFO) - most recent allocated will be the first to deallocate
2. Automatic memory management - memory is freed when function is returned
3. Limited lifetime - lifetime of the function call
4. fast allocation and deallocation - since it involves pointer adjustments
5. Limited size - of the size exceeds the stack, we get **stack overflow**

```cpp
void exampleFunction() {
    int a = 10;   // 'a' is allocated on the stack
    float b = 5.5; // 'b' is also allocated on the stack

    // Other code
} // 'a' and 'b' are automatically deallocated when the function exits
```

Stack based is efficent for short lived variables and function calls.

For larger memory use [[heap-mem |heap based memory]].
