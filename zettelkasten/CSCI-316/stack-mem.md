---
id: stack-mem
aliases: []
tags: []
---

# Stack memory

A memory allocation and deallocation using a stack data structure.

Usually used for managing local variables within functions and function management.

Each instance of a [[subroutines|subroutine]] at runtime has its own **frame** (activation record):

- frame pointer - points to a known location (address) of the current [[subroutines|subroutine]]
- return address
- function arguments
- local variables
- temporaries - hold immediate values from calculations,
- bookeeping - contains the [[subroutines|subroutine]]'s:
  - return address
  - the reference to the stack frame called the **dynamic link**.
- local variables, temporaries, and bookeeping have a negative **offset** from the frame pointer.
- function arguments and return usually have a positive **offset**

### Calling Sequence

Maintenance of the stack is the responsibility of the [[subroutines|subroutine]] **calling sequence**.

- the code executed by the user before and after the call
- the prologue (code executed at the beginning) [[subroutines|subroutine]]
- the epilogue (code executed at the end) of the [[subroutines|subroutine]]

![[stack-mem-demo.png]]

A typical calling sequence:

1. saves any caller-saves registers whose values may be needed after the call
2. computes the values of arguments and moves them into the stack or registers
3. computes the static link (if this is a language with nested subroutines), and
   passes it as an extra, hidden argument
4. uses a special subroutine call instruction to jump to the subroutine, simultaneously
   passing the return address on the stack or in a register

The prologue, calle:

1. allocates a frame by subtracting an appropriate constant from the sp
2. saves the old frame pointer into the stack, and updates it to point to the newly
   allocated frame
3. saves any callee-saves registers that may be overwritten by the current routine
   (including the static link and return address, if they were passed in registers)

The epilogue, subroutine complete:

1. moves the return value (if any) into a register or a reserved location in the stack
2. restores callee-saves registers if needed
3. restores the fp and the sp
4. jumps back to the return address

Finally, the caller

1. moves the return value to wherever it is needed
2. restores caller-saves registers if needed

The stack grow ==downwards== towards lower addresses for most language implementations.

![[stack-mem-demo2.png]]

Languages with nested [[subroutines|subroutine]] and static scoping, objects that lie in surrounding
[[subroutines|subroutine]], and are neither local or global can be maintained by a **static chain**.

- each stack frame contains a ==reference== to surrounding [[subroutines|subroutine]], called the **static link**.
- the ==value== of the frame pointer, which will be restored on the subroutine return, is called **dynamic link**.

As usual, dynamic links always point to the next frame down in the stack. Static links always
point down, but they may skip past many frames. They always point to the most recent
frame of the routine that statically encloses the current routine.

![[subroutine-nesting.png]]

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
