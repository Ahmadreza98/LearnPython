## Decorator

---

A decorator is a function that modifies the behavior of another function — 
without changing its code.

Think of it like:
> "Wrapping" a function to add extra features to it.

### Basic Structure

```
def my_decorator(func):
    def wrapper():
        print("Before the function runs")
        func()
        print("After the function runs")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
```

### Output:

```
Before the function runs
Hello!
After the function runs
```

The `@my_decorator` syntax is just a shortcut for:

```
say_hello = my_decorator(say_hello)
```