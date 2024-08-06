---
id: CSCI-316_Tao-Summer-2024
aliases: []
tags:
  - problem-set
  - fsm
  - regex
  - scopes
  - tree-traveral
  - code-snippets
  - tree-traversal
---

# Problem Sets

Collections of problems given by professor Tao.

- highly likely for questions from the book to be the exam questions.

> [!info]- **Summer 2024 Book**
> ![[Programming language pragmatics-Morgan Kaufmann.pdf]]

> [!question]- Chapter 2 Questions
>
> Write regular expressions to capture the following and draw the FSM.
>
> > [!question]+ Question 2.1/2.2 A ([[regex-and-cfg]])
> >
> > Strings in C. These are delimited by double quotes ("), and may not
> > contain newline characters. They may contain double-quote or backslash
> > characters if and only if those characters are “escaped” by a preceding
> > backslash. You may find it helpful to introduce shorthand notation to
> > represent any character that is not a member of a small specified set.
> >
> > > [!success]- solution
> > >
> > > The first quote starts the matching, **([^"\\] | \\.)** repeats for all characters
> > > that is not a double quote or escaped backslash and concatenate, where the Kleene
> > > star will concatenate until a double quote.
> > >
> > > **ANSWER:** `"(non-newline, ", \ | \\.)\*"` >
> > >
> > > **ANSWER:** `"([^"\\] | \\.)\*"`
> > >
> > > ```mermaid
> > > stateDiagram-v2
> > > direction LR
> > >
> > > [*] --> 1
> > > 1 --> 2: " (begin quote)
> > > 2 --> 3: newline
> > > 3 --> 2: \ (backslash)
> > > 2 --> 4: " (end quote)
> > > 4 --> [*]
> > > ```
>
> > [!question]+ Question 2.1/2.2 B
> >
> > Comments in Pascal. These are delimited by `(* and *)` or by `{ and }`.
> > They are not permitted to nest.
> >
> > > [!success]- solution
> > >
> > > **regex for `(* and *)`:** `\(\*[^*]*\*\)`
> > > Since both `(` and `*` have special meanings in regex, they need to be escaped with a `\`.
> > > This applies for the same for the closing `*` and the `)`.
> > > **`[^*]*`** will match(concatenate) characters that are not `*`, and will repeat til end.
> > >
> > > **regex for `{ and }`:** `\{[^}]*\}`
> > > Since `{` also have special meanings in regex, they need to be escaped with a `\`.
> > >
> > > **final regex:** `\(\*[^*]*\*\) | \{[^}]*\}`
> > >
> > > ```mermaid
> > > stateDiagram-v2
> > >
> > > [*] --> 1
> > > 1 --> 2: lparen
> > > 2 --> 3: asterisk
> > > 3 --> 3: non-asterisk
> > > 3 --> 4: asterisk
> > > 4 --> 5: rparen
> > > 5 --> [*]
> > > 4 --> 3: non-asterisk or rparen
> > > 1 --> 6: lbracket
> > > 6 --> 6: non rbracket
> > > 6 --> 7: rbracket
> > > 7 --> [*]
> > > ```
>
> > [!question]+ Question 2.1/2.2 C
> >
> > Numeric constants in C. These are octal, decimal, or hexadecimal integers,
> > or decimal or hexadecimal floating-point values. An octal integer begins
> > with 0, and may contain only the digits 0–7. A hexadecimal integer begins
> > with 0x or 0X, and may contain the digits 0–9 and a/A–f/F. A decimal
> > floating-point value has a fractional portion (beginning with a dot) or an
> > exponent (beginning with E or e). Unlike a decimal integer, it is allowed
> > to start with 0. A hexadecimal floating-point value has an optional
> > fractional portion and a mandatory exponent (beginning with P or p). In
> > either decimal or hexadecimal, there may be digits to the left of the dot,
> > the right of the dot, or both, and the exponent itself is given in decimal,
> > with an optional leading + or - sign. An integer may end with an optional
> > U or u (indicating “unsigned”), and/or L or l (indicating “long”) or LL or
> > ll (indicating “long long”). A floating-point value may end with an
> > optional F or f (indicating “float”—single precision) or L or l (indicating
> > “long”—double precision).
> >
> > > [!success]- octal integer solution
> > >
> > > - begins with 0 and can only contain digits 0-7.
> > >
> > >   **`0[0-7]+`**
> > >
> > > ```mermaid
> > > stateDiagram-v2
> > > direction LR
> > >
> > > [*] --> 1
> > > 1 --> 2: zero
> > > 2 --> 2: [0-7]
> > > 2 --> [*]
> > > ```
> >
> > > [!success]- hexadecimal integer solution
> > >
> > > - begins with 0x or 0X.
> > > - may contain digits from 0-9 and a/A-f/F.
> > >
> > >   **`0[xX]([0-9a-fA-F]+)([uU] | [lL])`**
> > >
> > > ```mermaid
> > > stateDiagram-v2
> > >
> > > [*] --> 1
> > > 1 --> 2: x or X
> > > 2 --> 3: 0-9 or a-f or A-F
> > > 3 --> 3: 0-9 or a-f or A-F
> > > 3 --> 4: u or U
> > > 3 --> 6: l or L
> > > 4 --> 5: l or L
> > > 5 --> [*]
> > > 6 --> [*]
> > >
> > > ```
> >
> > > [!success]- decimal floating-point solution
> > >
> > > - has numbers on both sides of the dot.
> > > - may have a exponent beginning with E or e.
> > > - may begin with a 0.
> > >
> > >   **`(([0-9]+[.][0-9]*)|([.][0-9]+)|([0-9]+[.][0-9]+))([eE][+-]?[0-9]+)?([fFlL])?`**
> > >
> > > ```mermaid
> > > stateDiagram-v2
> > >
> > > [*] --> 1
> > > 1 --> 2: [0-9]
> > > 2 --> 2: [0-9]
> > > 2 --> 3: dot
> > > 3 --> 4: [0-9]
> > > 4 --> 4: [0-9]
> > > 4 --> [*]
> > > 4 --> 7: e or E
> > > 7 --> 8: + or -
> > > 8 --> 9: [0-9]
> > > 9 --> 9: [0-9]
> > > 9 --> [*]
> > > 1 --> 5: dot
> > > 5 --> 6: [0-9]
> > > 6 --> 6: [0-9]
> > > 6 --> [*]
> > > 6 --> 10: e or E
> > > 10 --> 11: + or -
> > > 11 --> 12: [0-9]
> > > 12 --> 12: [0-9]
> > > 12 --> [*]
> > > ```
> >
> > > [!success]- hexadecimal floating-point solution
> > >
> > > - has a optional fractional portion.
> > > - mandatory exponent partion (beginning with P or p).
> > >
> > >   **`0[xX]([0-9a-fA-F]+[.][0-9a-fA-F]*){1}([pP][+-]?[0-9]+)([fFlL])?`**
> > >
> > > ```mermaid
> > > stateDiagram-v2
> > >
> > > [*] --> 1
> > > 1 --> 6
> > > 1 --> 2: x or X
> > > 2 --> 3: 0-9 or a-f or A-F
> > > 3 --> 3: 0-9 or a-f or A-F
> > > 3 --> 4: dot
> > > 4 --> 5: 0-9 or a-f or A-F
> > > 5 --> 5: 0-9 or a-f or A-F
> > > 5 --> 6: p or P
> > > 6 --> 7: + or -
> > > 7 --> 8: [0-9]
> > > 8 --> 9: f, F, l, L
> > > 9 --> [*]
> > > ```
>
> > [!question]+ Question 2.1/2.2 D
> >
> > Floating-point constants in Ada. These match the definition of real in
> > Example 2.3, except that (1) a digit is required on both sides of the
> > decimal point, (2) an underscore is permitted between digits, and (3) an
> > alternative numeric base may be specified by surrounding the
> > non-exponent part of the number with pound signs, preceded by a base in
> > decimal (e.g., 16#6.a7#e+2). In this latter case, the letters a . . f
> > (both upper- and lowercase) are permitted as digits. Use of these letters
> > in an inappropriate (e.g., decimal) number is an error, but need not be
> > caught by the scanner.
> >
> > > [!success]- solution
> > >
> > > ```mermaid
> > > stateDiagram-v2
> > >
> > > [*] --> 1: int
> > > 1 --> 2: [0-9]
> > > 2 --> 2: [0-9]
> > > 2 --> [*]
> > > 1 --> 3: real
> > > 3 --> 4: int
> > > 4 --> 5: e or E and + or - and [0-9]
> > > 5 --> 5: [0-9]
> > > 5 --> [*]
> > > 3 --> 6: decimal
> > > 6 --> 7: [0-9]
> > > 7 --> 8: (. [0-9] | [0-9] .)
> > > 8 --> 9: [0-9]
> > > 9 --> 9: [0-9]
> > > 9 --> [*]
> > > ```
>
> > [!question]+ Question 2.1/2.2 E
> >
> > Inexact constants in Scheme. Scheme allows real numbers to be explicitly
> > inexact (imprecise). A programmer who wants to express all constants
> > using the same number of characters can use sharp signs (#) in place of
> > any lower-significance digits whose values are not known. A base-10
> > constant without exponent consists of one or more digits followed by
> > zero of more sharp signs. An optional decimal point can be placed at the
> > beginning, the end, or anywhere in-between. (For the record, numbers in
> > Scheme are actually a good bit more complicated than this. For the
> > purposes of this exercise, please ignore anything you may know about
> > sign, exponent, radix, exactness and length specifiers, and complex or
> > rational values.)
> >
> > > [!success]- solution
> > >
> > > **regex:** digit$^+$ #$^*$ (. #$^*$ | Lambda ) | digit$^+$ . digit$^+$ #$^*$
> > >
> > > ```mermaid
> > > stateDiagram-v2
> > >
> > > [*] --> 1
> > > 1 --> 2: digits
> > > 2 --> 2: digits
> > > 2 --> 3: lambda
> > > 3 --> 3: #
> > > 3 --> 4: . (dot)
> > > 4 --> 4: #
> > > 4 --> 5: . (dot)
> > > 5 --> 6: digits
> > > 6 --> 6: digits
> > > 6 --> 7: lambda
> > > 7 --> 7: #
> > > 3 --> 8: lambda
> > > 8 --> 8: digits
> > > 8 --> 9: . (dot)
> > > 9 --> 6
> > > 7 --> [*]
> > > ```
>
> > [!question]+ Question 2.1/2.2 F
> >
> > Financial quantities in American notation. These have a leading dollar
> > sign ($), an optional string of asterisks (\*—used on checks to discourage
> > fraud), a string of decimal digits, and an optional fractional part
> > consisting of a decimal point (.) and two decimal digits. The string of
> > digits to the left of the decimal point may consist of a single zero (0).
> > Otherwise it must not start with a zero. If there are more than three
> > digits to the left of the decimal point, groups of three (counting from
> > the right) must be separated by commas (,). Example: $\*\*2,345.67. (Feel
> > free to use “productions” to define abbreviations, so long as the language
> > remains regular.)
> >
> > > [!success]- solution
> > >
> > > ```mermaid
> > > stateDiagram-v2
> > >
> > > [*] --> 1
> > > 1 --> 2: $
> > > 2 --> 3: *
> > > 3 --> 4: *
> > > 4 --> 5: 0
> > > 5 --> 6: lambda
> > > 5 --> 13: digit
> > > 13 --> 6: lambda
> > > 6 --> 7: lambda
> > > 6 --> 14: digit
> > > 6 --> 15: digit digit
> > > 7 --> 8: lambda
> > > 14 --> 8: lambda
> > > 15 --> 8: lambda
> > > 8 --> 8: , digit digit digit
> > > 8 --> 9: lambda
> > > 9 --> 10: . (dot)
> > > 9 --> 16: lambda
> > > 10 --> 11: digit
> > > 11 --> 12: digit
> > > 16 --> 12: lambda
> > > 12 --> [*]
> > > ```

> [!question]- Chapter 3 Questions
>
> > [!question]+ Question 3.6
> >
> > ```
> > procedure main()
> >   g : integer
> >   procedure B(a : integer)
> >       x : integer
> >       procedure A(n : integer)
> >           g := n
> >       procedure R(m : integer)
> >           write integer(x)
> >           x /:= 2 – – integer division
> >           if x > 1
> >               R(m + 1)
> >           else
> >               A(m)
> >       ––body of B
> >       x := a × a
> >       R(1)
> >   ––body of main
> >   B(3)
> >   write integer(g)
> > ```
> >
> > **
> > a) What does this program print?
> > b) Show the frames on the stack when A has just been called. For each
> > frame, show the static and dynamic links.
> > c) Explain how A finds g.
> > **
> >
> > > [!success]- solution to part a
> > >
> > > **prints:** 9, 4, 2, 3
> > >
> > > ```
> > > g is initialized
> > > B(3)
> > > ```
> > >
> > > ```
> > > x is initialized
> > > x /:= 2 => 9
> > > x > 1 (true) => R(m + 1)
> > > R(2)
> > > ```
> > >
> > > ```
> > > print(x) => 4
> > > x /:= 2 => 2
> > > x > 0 (true) => R(m + 1)
> > > R(3)
> > > ```
> > >
> > > ```
> > > print(x) => 2
> > > 2 /:= 2 => 0
> > > x > 0 (false) => A(m)
> > > A(3)
> > > ```
> > >
> > > ```
> > > g := n => 3
> > > print(g) => 3
> > > ```
> >
> > > [!success]- solution to part b
> > >
> > > ```mermaid
> > > classDiagram
> > > stack: A(3)
> > > stack: R(3)
> > > stack: R(2)
> > > stack: R(1)
> > > stack: B(3)
> > > stack: main
> > > ```
> > >
> > > main should be at the very bottom of the stack.
> >
> > > [!success]- solution to part c
> > >
> > > A is able to find g because of the enclosing scope or is a global variable.
>
> > [!question]+ Question 3.11
> >
> > Consider the following pseudocode:
> >
> > ```
> > procedure P(A, B : real)
> >     X : real
> >     procedure Q(B, C : real)
> >         Y : real
> >         . . .
> >     procedure R(A, C : real)
> >         Z : real
> >         . . . – – (_)
> >     . . .
> > ```
> >
> > Assuming static scope, what is the referencing environment at the location
> > marked by (\*)?
> >
> > > [!success]- solution
> > >
> > > - A is accessable form the produce P since it encloses R
> > > - C and Z is accessable from the produce of R

> [!question]- Chapter 4 Questions
>
> > [!question]+ Question 4.11
> >
> > Consider the following CFG for floating-point constants, without
> > exponential notation. (Note that this exercise is somewhat artificial: the
> > language in question is regular, and would be handled by the scanner of a
> > typical compiler.)
> >
> > ```
> > C --> digits . digits
> > digits --> digit more digits
> > more digits --> digits | empty
> > digit --> 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
> > ```
> >
> > Augment this grammar with attribute rules that will accumulate the value
> > of the constant into a val attribute of the root of the parse tree. Your
> > answer should be S-attributed.
> >
> > > [!success]- solution
> > >
> > > {C.val := digits$_1$.val . digits$_2$.val}
> > > {digits$_1$.val := digits$_2$.val and more_digits.val}
> > > {more_digits.val := digits.val}
> > > {more_digits.val := empty.val}
> > > {digit.val := 0}
> > > {digit.val := 1}
> > > {digit.val := 2}
> > > {digit.val := 3}
> > > {digit.val := 4}
> > > {digit.val := 5}
> > > {digit.val := 6}
> > > {digit.val := 7}
> > > {digit.val := 8}
> > > {digit.val := 9}

> [!question]- Chapter 6 Questions
>
> > [!question]+ Question 6.18 ([[tree-traversal]])
> > Revise the algorithm of Figure 6.6 so that it performs an in-order
> > enumeration, rather than preorder.
> >
> > ```java
> > class BinTree<T> implements Iterable<T> {
> >     BinTree<T> left;
> >     BinTree<T> right;
> >     T val;
> >     ...
> >
> >     // other methods: insert, delete, lookup, ...
> >
> >     public Iterator<T> iterator() {
> >         return new TreeIterator(this);
> >     }
> >     private class TreeIterator implements Iterator<T> {
> >         private Stack<BinTree<T>> s = new Stack<BinTree<T>>();
> >         TreeIterator(BinTree<T> n) {
> >             if (n.val != null) s.push(n);
> >         }
> >         public boolean hasNext() {
> >             return !s.empty();
> >         }
> >         public T next() {
> >             if (!hasNext()) throw new NoSuchElementException();
> >             BinTree<T> n = s.pop();
> >             if (n.right != null) s.push(n.right);
> >             if (n.left != null) s.push(n.left);
> >             return n.val;
> >         }
> >         public void remove() {
> >             throw new UnsupportedOperationException();
> >         }
> >     }
> > }
> > ```
> >
> > > [!success]- solution
> > >
> > > ```java
> > > class BinTree<T> implements Iterable<T> {
> > >
> > >   BinTree<T> left;
> > >   BinTree<T> right;
> > >   T val;
> > >   ...
> > >
> > >   // other methods: insert, delete, lookup, ...
> > >
> > >   public Iterator<T> iterator() {
> > >       return new TreeIterator(this);
> > >   }
> > >   private class TreeIterator implements Iterator<T> {
> > >       private Stack<BinTree<T>> s = new Stack<BinTree<T>>();
> > >       TreeIterator(BinTree<T> n) {
> > >           // solution
> > >           while (n.val != null) {
> > >               s.push(n);
> > >               n = n.left;
> > >           }
> > >       }
> > >       public boolean hasNext() {
> > >           return !s.empty();
> > >       }
> > >       public T next() {
> > >           if (!hasNext()) throw new NoSuchElementException();
> > >           BinTree<T> n = s.pop();
> > >           // inorder (solution)
> > >           while (n.right != null) {
> > >               s.push(n.right);
> > >               n = n.left;
> > >           }
> > >           return n.val;
> > >       }
> > >       public void remove() {
> > >           throw new UnsupportedOperationException();
> > >       }
> > >   }
> > > }
> > > ```
