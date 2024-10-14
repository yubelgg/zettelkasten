---
id: static-mem
aliases:
  - static
tags: []
---

## Static Memory

Memory allocation where the memory for a varibale or object is allocated at compile time.
It will have a fixed size and lifetime throughout the execution of the program.

Characteristics:

1. compile time allocation - memory is allocated before program starts
2. fixed size - memory that is allocated cannot be changed in size during the execution
3. lifetime - the allocated memory will exist for the entirety of the program
4. scope - static variable may be global or local, their lifetime is global --> 3

static variables declared with the `static` keyword within a [[subroutines |subroutine]] will retain
their value between function calls, since it is stored in static memory.

```cpp
#include <stdio.h>

void count() {
    static int counter = 0; // static variable
    counter++;
    printf("%d\n", counter);
}

int main() {
    count(); // prints 1
    count(); // prints 2
    count(); // prints 3
    return 0;
}
```

### Pros and Cons

pros:

- predictable memory usuage
- no runtime overhead for allocation and deallocation

cons:

- less flexibility, cannot change size
- higher memory usuage if allocated memory is not fully used
