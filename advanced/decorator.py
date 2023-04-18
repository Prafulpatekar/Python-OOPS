def mydecorator(function):
    def wrapper(*args,**kwargs):
        tests = function(*args,**kwargs)
        print("I am decorating your function!")
        return tests
    return wrapper

@mydecorator # New method to call
def example(arg):
    print(f"Demo for decorator : {arg}")

# example("jejj")# New method to call
# mydecorator(example)() # Old method to call


def logged(function):
    def wrapper(*args, **kwargs):
        value = function(*args, **kwargs)
        with open('decoarator.txt','+a') as f:
            f.write(f"Called by {function.__name__} and result: {value}\n")
        return value
    return wrapper

@logged
def get_logged(x,y):
    return x*y

# get_logged(2,5)

def timed(function):
    import time
    def wrapper(*args, **kwargs):
        before = time.time()
        value = function(*args, **kwargs)
        after = time.time()
        print(f"Before: {before} After:{after}")
    return wrapper

@timed
def iterator():
    for i in range(20):
        print(i)

iterator()