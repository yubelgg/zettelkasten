---
id: closure
aliases: []
tags: []
---

# Closure

## [[subroutines|subroutine]] closure

A closure is a programming concept where a subroutine (such as a function or method)
retains access to variables from its lexical scope even when the subroutine is executed
outside that scope.

![[subroutine-closure.png]]

```python
def make_multiplier(x):
    def multiplier(y):
        return x * y
    return multiplier

times_three = make_multiplier(3)
print(times_three(10))  # Outputs: 30

times_five = make_multiplier(5)
print(times_five(10))  # Outputs: 50
```

## pros and cons

pros:

- encapsulation

cons:

- memory management - if not handled carefully, it can lead to leaks
- complexity - understanding lifetimes and managing them properly can be complex

### first class value

First class status:

- it's passed as a parameter
- returned from a [[subroutines|subroutine]]
- assigned into a variable.

Second class status:

- value passed as a parameter, but not returned from a [[subroutines|subroutine]] or assigned into a variable

Third class status:

- cannot even be passed as a parameter
- ```c
  // C language example
  int main() {
      if (1 == 1) {
          // The if statement is a third-class value in C.
      }
      return 0;
  }
  ```

**Deep Binding** refers to binding free variables to the environment in which the
function was ==defined==.

```python
function makeCounter() {
    let count = 0; // count is a free variable for the inner function

    return function() {
        count++;
        return count;
    };
}

let counter = makeCounter();
console.log(counter()); // Outputs: 1
console.log(counter()); // Outputs: 2
```

**Shallow Binding** refers to binding free variables to the environment in which
the function was ==called==.

```
x : integer –– global variable

procedure makeClosure()
    x := 10
    return procedure() write(x)

procedure callClosure(cl)
    x := 20
    cl()

main()
    cl := makeClosure()
    callClosure(cl)  -- Outputs: 20 if shallow binding is used
```

### problem set

> [!questions]+ 3.14
> What does this program print if the language uses static scoping? What does
> it print with dynamic scoping? Why?
>
> ```
> x : integer – – global
>
> procedure set x(n : integer)
>     x := n
>
> procedure print x()
>     write integer(x)
>
> procedure first()
>     set x(1)
>     print x()
>
> procedure second()
>     x : integer
>     set x(2)
>     print x()
>     set x(0)
>
> first()
> print x()
> second()
> print x()
> ```
>
> output for static: 1, 1, 0, 1
> set_x(2) changes the global x due to static scope
> since the print_x() in second() is printing the local variable which is only initialized
>
> output for dynamic: 1, 1, 2, 1
> set_x(2) changes the local x due to dynamic scope
> since the print_x() in second() is printing the local variable which is changed b/c of dynamic scope

> [!questions]+ 3.19
> (a) What does this program print if the language uses static scoping?
> (b) What does it print if the language uses dynamic scoping with deep binding?
> (c) What does it print if the language uses dynamic scoping with shallow binding?
>
> ```
> x : integer := 1
> y : integer := 2
>
> procedure add()
>   x := x + y
>
> procedure second(P : procedure)
>   x : integer := 2
>   P()
>
> procedure first()
>   y : integer := 3
>   second(add)
>
> first()
> write integer(x)
> ```
>
> a) prints 3 since it adds the global x and y, updates global x
> b) prints 4 since it adds the local x which is 2 and global y which is 1, updates local and global x
> c) print 1 since global x + global y = 3, but that doesn't change global x
