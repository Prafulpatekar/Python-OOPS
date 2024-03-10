# 1) sort a given dictionary using dictionary comprehension

dic1 = {
    25: "cherry",
    30: "grapes",
    27: "orange",
    24: "banana",
    26: "mango",
    29: "pineapple",
    23: "apple",
    28: "watermelon",
}

# solution sorted by using key
dict2 = sorted(dic1)
newdic1 = {}
for d in dict2:
    newdic1[d] = dic1[d]
print(newdic1)

# solution sorted by using value
dict3 = {key:value for key,value in sorted(dic1.items(), key=lambda x: x[1])}

print(dict3)

