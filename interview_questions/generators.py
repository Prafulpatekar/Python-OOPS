# 1) generate a infinitely fibonacci number using generator

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

if __name__ == '__main__':
    f1 = fibonacci()
    print(next(f1))
    print(next(f1))
    print(next(f1))
    print(next(f1))
    print(next(f1))
    print(next(f1))
    print(next(f1))
    print(next(f1))
    print(next(f1))
    print(next(f1))
