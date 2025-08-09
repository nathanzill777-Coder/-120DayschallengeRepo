print("HELLO ESTEEMED USER!")
print("Press 1 for Addition")
print("Press 2 for Subtraction")
print("Press 3 for Multiplication")
print("Press 4 for Division")

option = int(input("Please enter the operation number you want to perform: "))

if option in [1, 2, 3, 4]:
    num1 = int(input("Enter 1st number: "))
    num2 = int(input("Enter 2nd number: "))

    if (option == 1):
        result = num1 + num2
    elif (option == 2):
        result = num1 - num2
    elif (option == 3):
        result = num1 * num2
    else:
        if (num2 == 0):
            print("Error: Division by zero is not allowed.")
            exit()
        result = num1 / num2  # float division

    print(f"The result of the operation is {result}")
else:
    print("Invalid operation entered.")
