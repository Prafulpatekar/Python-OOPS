numbers = [1,2,3,4,5,6,7,8,9,0]

# reversedList = []
# for index in range(len(numbers)):
#     reversedList.append(numbers[len(numbers) - index - 1])
# print(reversedList)


# numbers.reverse() # it is changing the  original list
# print(numbers)
# reversedList = list(reversed(numbers)) # # it is not changing the  original list
# print(reversedList)
reversedList = numbers[::-1]
print(reversedList)
