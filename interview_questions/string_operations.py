#1) write a code to check whether the a string is palindrome or not
s = "niti"

# solution 1
if s == s[::-1]:
    print("Yes Palindrome")
else:
    print("Not Palindrome")

# solution 2
x = 0
for i in range(len(s)):
    if s[i]!= s[-i-1]:
        x = 1
        break

if x == 0:
    print("yes Palindrome")
else:
    print("Not Palindrome")


# 2) Find the output 
input_str = "the sky is blue"
# output_str = "blue is the sky"
l = input_str.split()
l = l[::-1]
l = " ".join(l)
print(l)

# 3) Remove punctuation characters except the space using regex from a given string

str1  = "/*apple are & found% only! in @red & green."
s =""
for i in str1:
    if((i>="A" and i<="Z") | (i>="a" and i <="z") | (i==" ")):
        s += i 

print(s)

import re

def remove_punctuation_except_space(text):
    # Define a regular expression pattern to match any character that is not a space or alphanumeric
    pattern = r'[^\w\s]'
    
    # Use the sub() function from the re module to replace all matches of the pattern with an empty string
    clean_text = re.sub(pattern, '', text)
    
    return clean_text

# 4) Find a max repeat charcter in a string (Time Complexity should be less than O(n2))


def max_repeated_character(string = "abracadabra"):
    # Create a dictionary to store character frequencies
    char_count = {}
    
    # Iterate through the string and count occurrences of each character
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    # Find the character with the maximum frequency
    max_char = max(char_count, key=char_count.get)
    
    return max_char


if __name__ == '__main__':
    print(remove_punctuation_except_space("/*apple are & found% only! in @red & green."))
    print(max_repeated_character())