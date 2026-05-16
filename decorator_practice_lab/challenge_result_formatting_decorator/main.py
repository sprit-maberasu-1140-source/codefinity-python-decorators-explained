def uppercase_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result,str):
            return result.upper()
        return result
    return wrapper

@uppercase_result
def greet(name):
    return f"Hello, {name}!"

@uppercase_result
def farewell(name):
    return f"Goodbye, {name}."

print(greet("Alice"))
print(farewell("Bob"))
