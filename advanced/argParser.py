# Agrguments parser
import sys

# print(sys.argv[0]) # 0 positional argument is filename or program name
# print(sys.argv)

filename = sys.argv[1]
message = sys.argv[2]

with open(filename,'+w') as f:
    f.write(message)
