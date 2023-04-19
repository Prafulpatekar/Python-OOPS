import sys

def cube_generator(n):
    for x in range(n):
        yield x ** 3


# generator = cube_generator(9_00_00_000)
generator = cube_generator(100)
print(sys.getsizeof(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))

# for x in generator:
#     print(x)

# INFINITE Sequence

def infinite_sequence():
    result = 1
    while True:
        yield result
        result *= 5

values = infinite_sequence()
print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))