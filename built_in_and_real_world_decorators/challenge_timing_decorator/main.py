import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed = end_time - start_time
        print(f"Function '{func.__name__}' executed in {elapsed:.6f} seconds")
        return result
    return wrapper

@timing_decorator
def slow_add(a, b):
    time.sleep(0.1)
    return a + b

@timing_decorator
def fast_multiply(a, b):
    return a * b

slow_add(3, 7)
fast_multiply(4, 5)