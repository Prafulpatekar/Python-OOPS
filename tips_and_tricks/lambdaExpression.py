# Lambda Functions
# square = lambda x: x*x
# add = lambda x,y:x+y
# multipleAdd = lambda *args:sum(args)

# res=add(566,5)
# res=multipleAdd(5,5,3,532,23,2)

# print(res)
# print((lambda x: x**3)(5))

numbers = [2,55,4,62,31,45,23,10,86,97,11254,14,41,51,61]

even_numbers = list(filter(lambda x: x % 2 ==0,numbers))
sq_numbers = list(map(lambda x: x * x,numbers))
print(even_numbers)
print(sq_numbers)
