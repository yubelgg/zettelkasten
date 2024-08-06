---
id: heaps
aliases: []
tags:
  - dsa
  - code-snippets
---

# Heaps

A **heap** is a compelete [[binary-tree |binary tree]]:

- for every node, the value of its children is greater than or equal to its own value (min heap).
- for every node, the value of its children is less than or equal to its own value (max heap).

Common heap operations:

- insert
- return max/min of heap
- heapify

## Types of trees

1. Full Binary Tree

   - binary tree in which **each** parent has **exactly** two or no children.
   - ![[full-binary-tree.png]]

2. Perfect Binary Tree

   - binary tree in which **every** parent has **exactlyd** two children.
   - ![[perfect-binary-tree.png]]

3. Complete Binary Tree

   - every level is completely filled.
   - all left nodes must lean from the left.
   - last element doesn't have to have a right sibling (doesn't need to be a full binary tree).
   - ![[complete-binary-tree.png]]

```python
# Binary Tree in Python

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    # Traverse preorder
    def traversePreOrder(self):
        print(self.val, end=' ')
        if self.left:
            self.left.traversePreOrder()
        if self.right:
            self.right.traversePreOrder()

    # Traverse inorder
    def traverseInOrder(self):
        if self.left:
            self.left.traverseInOrder()
        print(self.val, end=' ')
        if self.right:
            self.right.traverseInOrder()

    # Traverse postorder
    def traversePostOrder(self):
        if self.left:
            self.left.traversePostOrder()
```
