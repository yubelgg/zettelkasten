---
id: decorators
aliases: []
tags: []
---

# Decorators

A decorator is a function that creates a "warper" around another function.

It is a function that takes another function and extends or modifies its behavior without
explicitly modifying its code.

```python
def my_decorator(func):
    def wrapper():
        print("comming from", func.__name__)
        return func()
    return wrapper

@my_decorator
def say_hello():
    print("hello")

say_hello()
```

outputs:

```
comming from say_hello
hello
```
