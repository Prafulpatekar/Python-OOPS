# sort a list without using sort keyword and with using sort keyword

l1 = [42,-52,5,2,45,5,0,69]
# l1.sort()

n = len(l1)

for i in range(n):
    for j in range(i+1,n):
        if l1[i] > l1[j]:
            l1[i], l1[j] = l1[j], l1[i]



print(l1)