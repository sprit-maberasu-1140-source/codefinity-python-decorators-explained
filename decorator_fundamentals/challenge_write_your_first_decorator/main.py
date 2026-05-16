def print_status(func):
    # Your code here
    def wrapper(*args,**kwargs):
        print("Function started")
        func(*args,**kwargs)
        print("Function ended")
    return wrapper

@print_status
def greet():
    print("Hello, world!")

@print_status
def add(a, b):
    print(a + b)

greet()
add(3, 4)
