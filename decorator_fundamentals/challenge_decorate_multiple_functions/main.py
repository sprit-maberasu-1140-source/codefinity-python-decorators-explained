def log_function_name(func):
    def wrapper(*args, **kwargs):
        print(func.__name__)
        return func(*args, **kwargs)
    return wrapper

@log_function_name
def greet(name):
    return f"Hello, {name}!"

@log_function_name
def add(a, b):
    return a + b

print(greet("Alice"))
print(add(3, 4))