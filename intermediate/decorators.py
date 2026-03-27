# Basic decorator

def uppercase_decorator(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper

@uppercase_decorator
def greet():
    return "hello world"

print(greet())

# Decorator with arguments

def repeat_decorator(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat_decorator(3)
def say_hi(name):
    print(f"Hi {name}!")

print("\nDecorator with arguments:")
say_hi("Eunice")