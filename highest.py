num1 = int(input("Please:Enter the 1st number"))
num2= int(input("Please:Enter the 2nd number"))
num3 = int(input("Please:Enter the 3rd number"))

if (num1>num2 and num1 >num3):
    print("{} is greatest among them".format(num1))
elif (num2>num1 and num2>num3):
    print("{} is greatest among the 3".format(num2))
else:
    print("{} is greatest".format(num3))