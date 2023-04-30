nums = [14,23,8,12,5,90]

def square(x):
    return x * x

squs = list(map(square,nums))
print(squs)
print(list(map(str,nums)))