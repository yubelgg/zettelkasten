---
id: linked-list
aliases: []
tags: []
---

# Linked List

## Dummy head approach

Linked List without dummy node:

```python
class ListNode:
    def __init__(self, value=0, next=None) {
        self.val = val
        self.next = next
    }

head = [2,1,3,5,6,4,7]

def solve() {
    if not head:
        return None

    dummy = ListNode()  # each next() will changed where head is pointing to
    curr = dummy        # return dummy since it points to the beginning
    head = head.next

    while head:
        curr.next = head
        curr = curr.next
        head = head.next

    return dummy
}

```

ListNode with dummy head:

```python
class ListNode:
    def __init__(self, value=0, next=None) {
        self.val = val
        self.next = next
    }

head = [2,1,3,5,6,4,7]

def solve() {
    if not head:
        return None

    dummy = ListNode()  # each next() will changed where head is pointing to
    curr = dummy        # return dummy since it points to the beginning

    while head:
        curr.next = head
        curr = curr.next
        head = head.next

    return dummy.next   # the first node will have no value
}

```

### Leetcode example

Leetcode 328:

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = ListNode()
        even = ListNode()

        odd_ptr = odd
        even_ptr = even
        index = 1

        while head:
            if index % 2 == 0:
                even_ptr.next = head
                even_ptr = even_ptr.next
            else:
                odd_ptr.next = head
                odd_ptr = odd_ptr.next
            head = head.next
            index += 1

        # so it terminates correctly and doesn't link back to any nodes in memory
        even_ptr.next = None
        odd_ptr.next = even.next
        return odd.next
```
