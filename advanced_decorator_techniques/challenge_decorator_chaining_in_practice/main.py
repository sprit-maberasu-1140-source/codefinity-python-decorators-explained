def add_two_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result +2
    return wrapper

def square_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result  **2
    return wrapper

@add_two_decorator
@square_decorator
def get_number():
    return 3

output = get_number()
print(output)
