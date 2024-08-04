---
id: priority-queue
aliases: []
tags:
  - dsa
  - code-snippets
---

# Priority Queue

A speical type of queue that is associated with a **priority value**, as opposed to a
normal queue **(first-in-first-out)**.

Priority queues can be implemented using an array, a linked list, a [[heaps]], or a
binary search tree. However, [[heaps]] data structure provides the most **efficient**
implementation of priority queues.

### Different implementation of priority queues

|     Operation      | peek | insert  | delete  |
| :----------------: | :--: | :-----: | :-----: |
|    Linked List     | O(1) |  O(n)   |  O(1)   |
|    Binary Heap     | O(1) | O(logn) | O(logn) |
| Binary Search Tree | O(1) | O(logn) | O(logn) |

### Operations on a priority queue heap

1. Inserting an element into the priority queue
   - will insert the new element at the end of the heap
   - will heapify depending on the if its a min or max heap (look at parent node and swap accordingly)
2. Deleting an element from the priority queue
   - select the element to be deleted
   - swap that element with the last element of the queue
   - remove the last element (delete())
   - then heapify the tree
3. Peeking the priority queue
   - will return the root of the queue
   - min or max depending on the type of heap (max heap or min heap)

```python
# Priority Queue implementation in Python

# Function to heapify the tree
def heapify(arr, n, i):
    # Find the largest among root, left child and right child
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    # Swap and continue heapifying if root is not largest
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

# Function to insert an element into the tree
def insert(array, newNum):
    size = len(array)
    if size == 0:
        array.append(newNum)
    else:
        array.append(newNum)
        for i in range((size // 2) - 1, -1, -1):
            heapify(array, size, i)

# Function to delete an element from the tree
def deleteNode(array, num):
    size = len(array)
    i = 0
    for i in range(0, size):
        if num == array[i]:
            break

    array[i], array[size - 1] = array[size - 1], array[i]

    array.remove(size - 1)

    for i in range((len(array) // 2) - 1, -1, -1):
        heapify(array, len(array), i)

arr = []

insert(arr, 3)
insert(arr, 4)
insert(arr, 9)
insert(arr, 5)
insert(arr, 2)

print ("Max-Heap array: " + str(arr))

deleteNode(arr, 4)
print("After deleting an element: " + str(arr))
```
