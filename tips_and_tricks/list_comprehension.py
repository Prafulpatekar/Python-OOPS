numbers = [18,22,24,13,15,62]
# result = []
# for n in numbers:
#     if n % 2 == 0:
#         result.append(n)
result = [n for n in numbers if n % 2 == 0]

nums = [1,2,3,4,5,6,7,8,9,10]
square = [n**2 for n in nums]

words = ['parrot','pen','scale','pencil','kite','laptop']
upper_words = [word.upper() if word.startswith('p') else word for word in words]
if __name__ =="__main__":
    print(result)
    print(square)
    print(upper_words)