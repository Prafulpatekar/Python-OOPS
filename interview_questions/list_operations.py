# 1) Print all the pairs with given sum

l = [8,7,5,2,3,1,4]

s = 11

for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i] + l[j] == s:
            print(l[i],l[j])


# 2) Find maximum and minimum values from the list without using max and min functions

l = [8,7,5,2,3,1,4]
maxium = l[0]
minimum = l[0]

# print(max(l))
# print(min(l))
for i in l:
    if i > maxium:
        maxium = i
    if i < minimum:
        minimum = i

print(maxium)
print(minimum)