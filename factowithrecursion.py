#finding the factorial of number
def factorial(x):
    if (x == 1):
        return 1
    else:
        return x* factorial(x-1)


number = int(input("Please:Enter the number you want to check"))

result = factorial(number)
print("Result is {}".format(result))
