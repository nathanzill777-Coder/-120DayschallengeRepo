#finding the factorial of number

number = int(input("Please:Enter the number you want to check"))

factorial = 1

if (number ==0):
    print("The factorial of {} is {}".format(number,factorial))
else:
    for i in range(1,number+1):
        factorial = factorial*i
    print("The factorial of {} is {}".format(number,factorial))  