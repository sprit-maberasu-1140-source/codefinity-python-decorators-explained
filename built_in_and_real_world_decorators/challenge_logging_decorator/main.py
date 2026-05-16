def log_calls(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        return func(*args, **kwargs)
    return wrapper

@log_calls
def add(a, b):
    return a + b

@log_calls
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

add(2, 3)
greet("Alice")
greet("Bob", greeting="Hi")