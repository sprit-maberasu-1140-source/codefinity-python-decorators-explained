def positive_integer_args(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg,int) or arg<=0:
                raise ValueError("All arguments must be positive integers.")
        for value in kwargs.values():
            if not isinstance(value,int) or value <=0:
                raise ValueError("All argments must be positive integers.")
                
        return func(*args, **kwargs)
    return wrapper

@positive_integer_args
def add(a, b):
    return a + b

@positive_integer_args
def multiply(a, b, c):
    return a * b * c

print(add(2, 3))
print(multiply(1, 2, 3))
