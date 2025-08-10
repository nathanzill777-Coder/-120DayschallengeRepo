#python program to display powers of 2 using for loop. 
#Display the numbers that are power of 2 using for loop.

# 2^1 = 2 , 2^2 =4 , 2^3 = 8 , 2^4 = 16 , 2^5 = 32 , 2^6 = 64.............2^0 =1.

number = int(input("Please:Enter the number of terms that you would want the program to print"))#7

if (number ==0):
    print("2 raised to the power of {} is 1".format(number))

for i in range (1,number+1):#what i mean by this is 1 to number.
    print("2 raised to the power of {} is {}".format(i,2**i))
