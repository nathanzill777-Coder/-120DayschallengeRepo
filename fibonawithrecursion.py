#lets do this again..

#This is fibonacci done with recursion function.

def fibonacci(i):
    if(i<=1):
        return i
    else:
        return fibonacci(i-1)+ fibonacci(i-2)

number = int(input("Please:Enter the number of terms you want"))

for i in range(0,number+1):#as stated earlier, we use number+1 because we are printing from get-go
    #this will start from the range 0 to the designated number
    #say we select the number as 10 .. number+1 will go 10 digits . So the range is from 0 to 10 in this way.
    print(fibonacci(i))
