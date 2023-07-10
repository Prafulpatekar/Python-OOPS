"""
Any and all Functions major functions
"""
import random
x = [True,False,False,False]
print(any(x))
print(all(x))

numbers = [random.randint(1,100) for x in range(10)]
numbers = [2,4,6,8]
even = lambda x: x % 2 ==0

result = [even(number) for number in numbers]


if all(result):
    print("All numbers are even")
else:
    print("Not all numbers are even")
    if any(result):
        print("At least on number is even")
    else:
        print("No number is even")

