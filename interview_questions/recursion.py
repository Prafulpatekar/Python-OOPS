def factorial(number):
    if number == 0 or number==1:
        return 1
    return number * factorial(number-1)

def fibonacci(number):
    if number == 0 or number==1:
        return number
    return fibonacci(number-1) + fibonacci(number-2)

def sum_of_digits(number):
    if number < 10 :
        return number
    first_digit = number // 10**(len(str(number))-1) # quotient //
    rest_digits = number % (10**(len(str(number))-1)) # remainder %
    return first_digit + sum_of_digits(rest_digits)

if __name__ =="__main__":
    # print(factorial(0))
    # print(fibonacci(5))
    print(sum_of_digits(123))