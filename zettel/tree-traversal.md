---
id: tree-traversal
aliases: []
tags:
  - tree-traversal
  - code-snippets
---

# Tree traversal

Most known tree traversals are preorder, inorder, and postorder.

Preorder visits nodes from the root to the left then to the right.
==root --> left --> right==
![[preorder-traversal.png]]

> [!example]- Preorder traversal using recursion
>
> ```java
> class Node {
>     int data;
>     Node left, right;
>     public Node(int item) {
>         data = item;
>         left = right = null;
>     }
> }
>
> public class GfG {
>     // Function to perform preorder traversal
>     static void preorderTraversal(Node node) {
>
>         // Base case
>         if (node == null)
>             return;
>
>         // Visit the current node
>         System.out.print(node.data + " ");
>
>         // Recur on the left subtree
>         preorderTraversal(node.left);
>
>         // Recur on the right subtree
>         preorderTraversal(node.right);
>     }
>
>     public static void main(String[] args) {
>         Node root = new Node(1);
>         root.left = new Node(2);
>         root.right = new Node(3);
>         root.left.left = new Node(4);
>         root.left.right = new Node(5);
>         preorderTraversal(root);
>     }
> }
> ```

> [!example]- Preoder traversal with an iterable
>
> ```java
> import java.util.Stack;
>
> // A binary tree node
> class Node {
>     int data;
>     Node left, right;
>
>     Node(int item) {
>         val = item;
>         left = right = null;
>     }
> }
>
> class BinaryTree {
>   Node root;
>
>   void iterativePreorder() {
>         iterativePreorder(root);
>   }
>
>   void iterativePreorder(Node node) {
>       if (node == null) {
>           return;
>       }
>
>       Stack<Node> s = new Stack<Node>();
>       s.push(root);
>
>       while (s.empty() == false) {
>           // Pop the top item from stack and print it
>           Node n = s.pop();
>
>           // Push right and left children of the popped node to stack
>           if (n.right != null) {
>               s.push(n.right);
>           }
>           if (n.left != null) {
>               s.push(n.left);
>           }
>
>           return n.val
>       }
>   }
>
>   public static void main(String args[]) {
>       BinaryTree tree = new BinaryTree();
>       tree.root = new Node(10);
>       tree.root.left = new Node(8);
>       tree.root.right = new Node(2);
>       tree.root.left.left = new Node(3);
>       tree.root.left.right = new Node(5);
>       tree.root.right.left = new Node(2);
>       tree.iterativePreorder();
>   }
> }
> ```

Inorder traversal visits the nodes from left, to root, then to the right.
==left --> root --> right==
![[inorder-traversal.png]]

> [!example]- Inorder Traversal with recursion
>
> ```java
> class Node {
>   int data;
>   Node left, right;
>
>   public Node(int item) {
>       data = item;
>       left = right = null;
>   }
> }
>
> class GfG {
>   // Function to perform inorder traversal
>   static void inorderTraversal(Node node) {
>
>   // Base case
>   if (node == null)
>       return;
>
>   // Recur on the left subtree
>   inorderTraversal(node.left);
>
>   // Visit the current node
>   System.out.print(node.data + " ");
>
>   // Recur on the right subtree
>   inorderTraversal(node.right);
> }
>
>   public static void main(String[] args) {
>       Node root = new Node(1);
>       root.left = new Node(2);
>       root.right = new Node(3);
>       root.left.left = new Node(4);
>       root.left.right = new Node(5);
>       inorderTraversal(root);
>   }
> }
> ```

Postorder traversal visits nodes from the left, to right, to root
==left --> right --> root==
![[postorder-traversal.png]]

> [!example]- Postorder traversal using recursion
>
> ```java
> class Node {
>   int data;
>   Node left, right;
>   public Node(int item) {
>       data = item;
>       left = right = null;
>   }
> }
>
> public class GfG {
>   static void postorderTraversal(Node node) {
>
>       // Base case:
>       if (node == null)
>           return;
>
>       // Recur on the left subtree
>       postorderTraversal(node.left);
>
>       // Recur on the right subtree
>       postorderTraversal(node.right);
>
>       // Visit the current node
>       System.out.print(node.data + " ");
>   }
>
>   public static void main(String[] args) {
>       Node root = new Node(1);
>       root.left = new Node(2);
>       root.right = new Node(3);
>       root.left.left = new Node(4);
>       root.left.right = new Node(5);
>       postorderTraversal(root);
>   }
> }
> ```
