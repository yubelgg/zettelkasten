---
id: heap-mem
aliases:
  - heap based memory
tags: []
---

# Heap memory allocation

Heap based allocation allows for more flexiability and complex memory management.
It's suitable for data that needs to persist beyound just the function scope.

## Characteristics

1. Dynamic allocation - memory allocated during runtime, flexiability
2. Manual management - programmer is responsible for the allocation and deallocation
3. Persistent lifetime - allow data to exist beyond the a single function scope
4. Variable size - size can vary depending on the type of data structure
5. Heap frammentation - can lead to inefficent memory and slower allocation

```cpp
#include <iostream>

int main() {
    // Allocate memory for an integer on the heap
    int* p = new int;

    // Assign a value to the allocated memory
    *p = 42;

    // Use the allocated memory
    std::cout << *p << std::endl;

    // Deallocate the memory when done
    delete p;

    return 0;
}
```

Heap-based allocation is commonly used for large or complex data structures,
such as linked lists, [[binary-tree|trees]], and graphs, or when the size of the data structure
cannot be determined until runtime.
