---
id: problem-set
aliases:
  - unformatted solution
tags: []
---

### Chapter 3 Questions

**Question 3.1** ([[binding-time |binding time]])
Indicate the binding time (when the language is designed, when the program is linked, when
the program begins execution, etc.) for each of the following decisions in your favorite
programming language and implementation. Explain any answers you think are open to
interpretation.

- The number of built-in functions (math, type queries, etc.)
- The variable declaration that corresponds to a particular variable reference (use)
- The maximum length allowed for a constant (literal) character string The referencing
  environment for a subroutine that is passed as a parameter
- The address of a particular library routine
- The total amount of space occupied by program code and data

> [!success]+ solution
>
> 1. This decision is made when the **C++** language was designed, the creators of the
>    language determine the amount of **built-in** functions. Once the decision is
>    made it will remain constant throughout the lifecycle of the language or program.
>    So it will not change **during the compilation or execution**.
> 2. **Declaring** a variable in **C++**, it tells the compiler the name and type. **During
>    compilation**, the compiler will associate the declaration with memory address. The
>    binding time occurs before **execution**.
> 3. The binding time for the maximum length allowed for a constant (literal) character
>    string is when the language is designed or specified. Decision is typically set
>    during the language design and remains **constant** throughout program **compilation and execution**.
> 4. The binding time for referencing the subroutine environment is known at **compile
>    time**. As all address for declaration is known at during **compilation**.
> 5. During the **linking phase**, addresses of external library routines are resolved
>    to actual memory locations, allowing the program to reference and use these
>    routines correctly **during execution**.
> 6. The binding time for the total amount of space occupied by program code and
>    data **can vary**. The space occupied by program code is determined **during
>    compilation**, while the space occupied by data can be determined either at
>    **compile time (for statically allocated data) or at runtime (for dynamically
>    allocated data)**. So, it involves a **combination of compile-time and runtime**
>    binding decisions.

**Questions 3.2**
In Fortran 77, local variables were typically allocated statically. In Algol and its descendants
(e.g., Ada and C), they are typically allocated in the stack. In Lisp they are typically allocated
at least partially in the heap. What accounts for these differences? Give an example of a
program in Ada or C that would not work correctly if local variables were allocated statically.
Give an example of a program in Scheme or Common Lisp that would not work correctly if
local variables were allocated on the stack.

> [!success]+ solution
>
> - Static allocation of local variables allowed for faster access and manipulation of
>   data, as the compiler could optimize memory usage and reduce runtime overhead.
> - Stack allocation of local variables allowed for more flexible memory management
>   and better control over memory usage. Additionally, stack allocation simplified the
>   process of calling and returning from functions, as the stack could be used to
>   store local variables, function arguments, and return addresses.
> - Heap allocation of local variables allowed for more dynamic and flexible memory
>   management, as Lisp programs often manipulate complex data structures and
>   create and destroy objects at runtime.
> - in a subroutine, if local variables were allocated statically, they can only be used
>   once or have the correct value.
> - if local variables were allocated on stack then recusive calls to can overwrite
>   variable values.

**Questions 3.4**
Give three concrete examples drawn from programming languages with
which you are familiar in which a variable is live but not in scope.

> [!success]+ solution
>
> ```cpp
> #include <stdio.h>
> int main() {
>   int x = 2;
>   if (x > 1) {
>       int y = x++;
>   }
>   printf("%d\n", y); // result in an error due to 'y' being out of scope
>   return 0;
> }
> ```
>
> ```python
> def foo() {
>   x = 2
>   if x > 1:
>       y = x + 1
>   print(y)    # y is out of scope
> }
> ```
>
> ```java
> public class ScopeExample {
>   public static void main(String[] args) {
>       int x = 15;
>       if (x > 10) {
>           int z = x * 3;
>       }
>       System.out.println(z); // result in an error, 'z' out of scope
>   }
> }
> ```

**Question 3.6**

```pseudocode
procedure main()
  g : integer
  procedure B(a : integer)
      x : integer
      procedure A(n : integer)
          g := n
      procedure R(m : integer)
          write integer(x)
          x /:= 2 – – integer division
          if x > 1
              R(m + 1)
          else
              A(m)
      ––body of B
      x := a × a
      R(1)
  ––body of main
  B(3)
  write integer(g)
```

**
a) What does this program print?
b) Show the frames on the stack when A has just been called. For each
frame, show the static and dynamic links.
c) Explain how A finds g.
**

> [!success]- solution to part a
> **prints:** 9, 4, 2, 3
>
> ```
> g is initialized
> B(3)
> ```
>
> ```
> x is initialized
> x /:= 2 => 9
> x > 1 (true) => R(m + 1)
> R(2)
> ```
>
> ```
> print(x) => 4
> x /:= 2 => 2
> x > 0 (true) => R(m + 1)
> R(3)
> ```
>
> ```
> print(x) => 2
> 2 /:= 2 => 0
> x > 0 (false) => A(m)
> A(3)
> ```
>
> ```
> g := n => 3
> print(g) => 3
> ```

> [!success]- solution to part b
>
> ```mermaid
> classDiagram
> stack: A(3)
> stack: R(3)
> stack: R(2)
> stack: R(1)
> stack: B(3)
> stack: main
> ```
>
> main should be at the very bottom of the stack.

> [!success]- solution to part c
> A is able to find g because of the enclosing scope or is a global variable.

**Question 3.7**
Accustomed to Java, new team member Brad includes the following
code in the main loop of his program:

Before:

```c
list_node* L = 0;
while (more_widgets()) {
    L = insert(next_widget(), L);
}
L = reverse(L)
```

After:

```c
list_node* L = 0;
while (more_widgets()) {
    L = insert(next_widget(), L);
}
list_node* T = reverse(L);
delete_list(L);
L = T;
```

Sadly, after running for a while, Brad’s program always runs out of memory and crashes.
Explain what’s going wrong

This seems to solve the insufficient memory problem, but where the program used to
produce correct results (before running out of memory), now its output is strangely
corrupted, and Brad goes back to Janet for advice. What will she tell him this time?

> [!success]+ solution
> In java, memory locations not pointed to by a variable, is removed by garbage
> collection. Brad creating whole new list each time with reverse, filling up
> the memory, and in **C** there is no garbage collection that will free up memory
>
> In the delete function, we are just doing a free(t->data), which means the widget
> dynamic data will be deleted. Note: in insert function, we have created the memory for
> the node, not for the data which data pointer is pointing to. The pointer to data is
> provided to us by next_widget() function.
>
> In Reverse function, when we create a new node, we pass the data function reference
> to new node. So basically L1 and L2, nodes of both lists are pointing to the same data
> reference. now if in delete_list(L) i delete the free(t->data) then that data is deleted and
> this change will be visible from the newly created reversed list also because that also
> refeences the same. Hence the output is random and corrupted.

**Question 3.9**

```c
{ int a, b, c;
    ...
    { int d, e;
        ...
        { int f;
        ...
        }
    ...
    }
    ...
    { int g, h, i;
        ...
    }
    ...
}
```

a) Assume that each integer variable occupies four bytes. How much total space is required
for the variables in this code?

> [!success]+ solution
> total 9 variables \* four bytes = 36 bytes

(b) Describe an algorithm that a compiler could use to assign stack frame offsets to the
variables of arbitrary nested blocks, in a way that minimizes the total space required.

> [!success]+ solution
> using recursion to traverse through each nested scope. Once out of the scope the
> stack will keep the outer scoped variables in the stack and move on the next scope of
> nested variables

**Question 3.11**

Consider the following pseudocode:

```
procedure P(A, B : real)
X : real
    procedure Q(B, C : real)
        Y : real
        . . .
    procedure R(A, C : real)
        Z : real
        . . . – – (\*)
        . . .
```

Assuming static scope, what is the referencing environment at the location
marked by (\*)?

> [!success]- solution
>
> - A is accessable form the produce P since it encloses R
> - C and Z is accessable from the produce of R

**Questions 3.14** ([[closure]])
What does this program print if the language uses static scoping? What does
it print with dynamic scoping? Why?

```
x : integer – – global
procedure set x(n : integer)
    x := n
procedure print x()
    write integer(x)
procedure first()
    set x(1)
    print x()
procedure second()
    x : integer
    set x(2)
    print x()
    set x(0)
first()
print x()
second()
print x()
```

> [!success]+ solution
> output for static: 1, 1, 0, 1
> set_x(2) changes the global x due to static scope
> since the print_x() in second() is printing the local variable which is only initialized

> [!success]+ solution
> output for dynamic: 1, 1, 2, 1
> set_x(2) changes the local x due to dynamic scope
> since the print_x() in second() is printing the local variable which is changed b/c of dynamic scope

**Question 3.19** ([[closure]])
(a) What does this program print if the language uses static scoping?
(b) What does it print if the language uses dynamic scoping with deep binding?
(c) What does it print if the language uses dynamic scoping with shallow binding?

```
x : integer := 1
y : integer := 2
procedure add()
  x := x + y
procedure second(P : procedure)
  x : integer := 2
  P()
procedure first()
  y : integer := 3
  second(add)
first()
write integer(x)
```

> [!success]+ solution
> a) prints 3 since it adds the global x and y, updates global x
> b) prints 4 since it adds the local x which is 2 and global y which is 1, updates local and global x
> c) print 1 since global x + global y = 3, but that doesn't change global x

**Question 3.20**
Consider mathematical operations in a language like C++, which supports both overloading
and coercion. In many cases, it may make sense to provide multiple, overloaded versions of
a function, one for each numeric type or combination of types. In other cases, we might use
a single version probably defined for double-precision floating point arguments—and rely on
coercion to allow that function to be used for other numeric types (e.g., integers). Give an
example in which overloading is clearly the preferable approach. Give another in which
coercion is almost certainly better.

> [!success]+ solution
> In the case of overloading - max function
>
> ```cpp
> int max(int a, int b) {
>   return (a > b) ? a : b;
> }
> double max(double a, double b) { # better precision
>   return (a > b) ? a : b;
> }
> // Usage
> int maxInt = max(5, 10);
> double maxDouble = max(3.14, 2.71);
> ```
>
> In the case of coercion
>
> ```cpp
> double sqrt(double x) {
>   // Implementation of square root calculation
> }
> // Usage
> double result = sqrt(25); // Double precision
> float result_float = sqrt(25.0f); // Float precision
> ```

### Chapter 4 Questions

**Question 4.11**
Consider the following CFG for floating-point constants, without
exponential notation. (Note that this exercise is somewhat artificial: the
language in question is regular, and would be handled by the scanner of a
typical compiler.)

```
C --> digits . digits
digits --> digit more digits
more digits --> digits | empty
digit --> 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9

```

Augment this grammar with attribute rules that will accumulate the value
of the constant into a val attribute of the root of the parse tree. Your
answer should be S-attributed.

> [!success]- solution
> {C.val := digits$_1$.val . digits$_2$.val}
> {digits$_1$.val := digits$_2$.val and more_digits.val}
> {more_digits.val := digits.val}
> {more_digits.val := empty.val}
> {digit.val := 0}
> {digit.val := 1}
> {digit.val := 2}
> {digit.val := 3}
> {digit.val := 4}
> {digit.val := 5}
> {digit.val := 6}
> {digit.val := 7}
> {digit.val := 8}
> {digit.val := 9}

### Chapter 6 Questions

**Question 6.1**
We noted in Section 6.1.1 that most binary arithmetic operators are left associative in most
programming languages. In Section 6.1.4, however, we also noted that most compilers are
free to evaluate the **operands** of a binary operator in either order. Are these statements
contradictory? Why or why not?

> [!success]+ solution
>
> - left-associativity and the order of operand evaluation are related concepts but not contradictory.
> - while left-associative means evaluating left to right for an expression with multiple
>   instance of the same **operator**
> - the compiler may choose to evaluate the **operands** a and b in different orders
>   but these does not contradict left-associative that only groups the **operands**

**Question 6.2**
As noted in Figure 6.1, Fortran and Pascal give unary and binary minus the same level of
precedence. Is this likely to lead to nonintuitive evaluations of certain expressions? Why or why not?

> [!success]+ solution
> This will lead to nonintuitive evaluation
>
> - -2 \* 7
> - -(2 \* 7)

**Question 6.4**
Translate the following expression into postfix and prefix notation:
[−b + sqrt(b × b − 4 × a × c)]/(2 × a)

> [!success]+ solution
> Prefix notation: / + - b sqrt - \* b b \* 4 a c \* 2 a.
> Postfix notation: b - b b \* 4 a c \* - sqrt + 2 a \* /

**Question 6.7**
Is &(&i) ever valid in C? Explain.

> [!success]+
> it is not valid. The & operator requires its operand to be an lvalue, a memory location
> that can be accessed by the program. The expression &i yields the address of the
> variable i, which is an rvalue and cannot be used as an operand of &.

**Question 6.8**
Languages that employ a reference model of variables also tend to employ automatic
garbage collection. Is this more than a coincidence? Explain.

> [!success]+ solution
> It is not a coincidence. Languages that employ a reference model of variables (i.e.,
> variables that refer to memory locations rather than containing values directly) require
> a mechanism for deallocating unused memory, since the programmer does not have
> direct control over when memory is no longer needed. Garbage collection automatically
> identifies and frees memory that is no longer being used by the program.

**Question 6.12**
Describe a plausible scenario in which a programmer might wish to avoid short-circuit
evaluation of a Boolean expression

> [!question]+ solution
> if a program need to print or log some in each iteration, so don't exit the loop

**Question 6.18 ([[tree-traversal]])**
Revise the algorithm of Figure 6.6 so that it performs an in-order
enumeration, rather than preorder.

```java
class BinTree<T> implements Iterable<T> {
    BinTree<T> left;
    BinTree<T> right;
    T val;
    ...

    // other methods: insert, delete, lookup, ...

    public Iterator<T> iterator() {
        return new TreeIterator(this);
    }
    private class TreeIterator implements Iterator<T> {
        private Stack<BinTree<T>> s = new Stack<BinTree<T>>();
        TreeIterator(BinTree<T> n) {
            if (n.val != null) s.push(n);
        }
        public boolean hasNext() {
            return !s.empty();
        }
        public T next() {
            if (!hasNext()) throw new NoSuchElementException();
            BinTree<T> n = s.pop();
            if (n.right != null) s.push(n.right);
            if (n.left != null) s.push(n.left);
            return n.val;
        }
        public void remove() {
            throw new UnsupportedOperationException();
        }
    }
}
```

> [!success]- solution
>
> ```java
> class BinTree<T> implements Iterable<T> {
>   BinTree<T> left;
>   BinTree<T> right;
>   T val;
>   ...
>   // other methods: insert, delete, lookup, ...
>
>   public Iterator<T> iterator() {
>       return new TreeIterator(this);
>   }
>   private class TreeIterator implements Iterator<T> {
>       private Stack<BinTree<T>> s = new Stack<BinTree<T>>();
>       TreeIterator(BinTree<T> n) {
>           // solution
>           while (n.val != null) {
>               s.push(n);
>               n = n.left;
>           }
>       }
>       public boolean hasNext() {
>           return !s.empty();
>       }
>       public T next() {
>           if (!hasNext()) throw new NoSuchElementException();
>           BinTree<T> n = s.pop();
>           // inorder (solution)
>           while (n.right != null) {
>               s.push(n.right);
>               n = n.left;
>           }
>           return n.val;
>       }
>       public void remove() {
>           throw new UnsupportedOperationException();
>       }
>   }
> }
> ```

## Chapter 7

**Question 7.1**
Most statically typed languages developed since the 1970s (including Java, C#, and the
descendants of Pascal) use some form of name equivalence for types. Is structural
equivalence a bad idea? Why or why not?

> [!solution]+ solution
> whether structural equivalence is a bad idea is up to the programmer preference and
> the language design. Structural equivalence may offer more flexability for the
> trade off of explicitness.

**Question 7.2**
In the following code, which of the variables will a compiler consider to have compatible
types under structural equivalence? Under strict name equivalence? Under loose name equivalence?

```
type T = array [1..10] of integer
S = T
A : T
B : T
C : S
D : array [1..10] of integer
```

> [!success]+ solution
> All four arrays are structurally equivalent. Under name equivalence, array D is
> incompatible with the others. Under strict name equivalence A and B are also
> incompatible with C; under loose name equivalence A, B, and C are all mutually compatible.

**Question 7.3**
Consider the following declarations:

```
1. type cell    –– a forward declaration
2. type cell ptr = pointer to cell
3. x : cell
4. type cell = record
5.   val : integer
6.   next : cell ptr
7. y : cell
```

Should the declaration at line 4 be said to introduce an alias type? Under strict name
equivalence, should x and y have the same type? Explain

> [!success]+ solution
> It should not since in line 1 it is only a declaration thats not defined.
> Variable x and y share the same definition that is defined on line 4, so they are the same type.

## Chapter 8 ([[struct-records |struct and records]])

**Question 8.1**
Suppose we are compiling for a machine with 1-byte characters, 2-byte shorts, 4-byte
integers, and 8-byte reals, and with alignment rules that require the address of every
primitive data element to be an even multiple of the element’s size. Suppose further that the
compiler is not permitted to reorder fields. How much space will be consumed by the
following array? Explain.

```
A : array [0..9] of record
s : short
c : char
t : short
d : char
r : real
i : integer
```

> [!success]+ solution
> s: range n to n+2
> c: range n+2 to n+3
> t: range n+4 to n+6 <-- 3 is odd, have to skip to 4
> d: range n+6 to n+7
> r: range n+8 to n+16 <-- starts at 8 since its odd
> i: range n+16 to n+20
> we need at least 20 bytes for this struct
> so we add 4 bytes for padding
> total => 24 \* 10 = 240

**Question 8.16** ([[pointers]])
Explain the meaning of the following C declarations:
double \*a[n];
double (\*b)[n];
double (\*c[n])();
double (\*d())[n];

> [!success]+ solution
> double \*a[n] - declares an array of n pointers of doubles
> double (\*b)[n] - pointer to an array of n doubles
> double (\*c[n])() - array of n pointers that returns a function of doubles
> double (\*d())[n] - function returning pointers to array of n doubles

## Chapter 9

**Question 9.4**
Consider the following (erroneous) program in C:

```cpp
void foo() {
    int i;
    printf("%d ", i++);
}
int main() {
    int j;
    for (j = 1; j <= 10; j++) foo();
}
```

Local variable i in subroutine foo is never initialized. On many systems, however, the
program will display repeatable behavior, printing 0 1 2 3 4 5 6 7 8 9. Suggest an
explanation. Also explain why the behavior on other systems might be different, or
nondeterministic.

> [!success]+ solution
>
> - In many systems, local variables are allocated in [[stack-mem |stack]]
> - When local variables are not explicitly initialized, value is indeterminate and
>   will contain what was previous stored at memory location of the stack
> - The behavior will be different or nondeterministic from other systems because
>   the way uninitialized variables are handled by the compilers.
> - Different compilers may optimize uninitialized variables differently
> - example is they may not place uninitialized variables in the data section

**Question 9.15**
Consider the following declaration in C:
**double (\*foo (double (\*) (double, double[]), double)) (double, ...);**
Descrilbe in English the type of foo.

> [!success]+ solution
>
> - **double(\*foo(...)):** foo is a pointer to a function that returns a double
> - arg of **foo()** is a **double(\*)(double,double[])**, where **foo** expects
>   a single argument which is a **pointer** to another function that returns a double
> - the first parameter takes in a double, the second is an array of doubles
> - **(...)** at the end will take in multiple arguments of doubles, **variadic** function (spread operator)

**Question 9.16**
Does a program run faster when the programmer leaves optional parameters out of a
subroutine call? Why or why not?

> [!success]+ solution
> No it does not since those optional args have default values

**Question 9.17**
Why do you suppose that variable-length argument lists are so seldom supported by high-
level programming languages?

> [!success]+ solution
>
> - Fixed argument lists make it easier for the compiler to check types at compile-
>   time, reducing runtime errors.
> - Variable-length arguments can introduce ambiguity and make type checking more
>   complex, but potentially leading to runtime type errors that are harder to debug.
> - Variable-length arguments can add complexity to the compiler's implementation.
> - Functions with a fixed number of arguments are generally easier to read and understand.

**Question 9.20**
Describe a plausible implementation of C++ destructors or Java try. . .
finally blocks. What code must the compiler generate, at what points
in the program, to ensure that cleanup always occurs when leaving a scope?

> [!success]+ solution
>
> ```cpp
> #include<iostream.h>
> class example//class defnition {
>     public:
>         example() {     // constructor
>             cout<<"constructor";
>         }
>         ~example() {    // destructor
>             cout<<"destructor";
>         }
> }
> void main() {
>     example obj;//constructor due to object created
>     cout<<"constructor created successfully";//main class output generated
> }
> ```
