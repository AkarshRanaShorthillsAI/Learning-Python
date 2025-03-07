# Python Closures, Scope, and Decorators

# 1. Scope Examples

def local_scope_example():
    x = 10  # Local variable
    print("Local Scope:", x)

local_scope_example()

# Enclosing Scope

def outer_function():
    y = 20
    def inner_function():
        nonlocal y  # Accessing enclosing scope variable
        y += 5
        print("Enclosing Scope:", y)
    inner_function()

outer_function()

# Global Scope
global_var = 30

def access_global():
    global global_var
    global_var += 10
    print("Global Scope:", global_var)

access_global()

# 2. Closure Example

def outer_function(msg):
    def inner_function():
        print("Closure Message:", msg)
    return inner_function

closure_example = outer_function("Hello, Closure!")
closure_example()

# 3. Decorator Examples

def decorator_function(original_function):
    def wrapper_function():
        print("Wrapper executed before:", original_function.__name__)
        return original_function()
    return wrapper_function

@decorator_function
def say_hello():
    print("Hello!")

say_hello()

# Class Decorator

def class_decorator(cls):
    class NewClass(cls):
        def __init__(self, *args, **kwargs):
            print("Class is being decorated")
            super().__init__(*args, **kwargs)
    return NewClass

@class_decorator
class SampleClass:
    def __init__(self):
        print("SampleClass instance created")

sample = SampleClass()

# Built-in Decorator Example

class Sample:
    def __init__(self, value):
        self._value = value

    @property
    def value(self):
        return self._value

obj = Sample(100)
print("Property Decorator Value:", obj.value)
