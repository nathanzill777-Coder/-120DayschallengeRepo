#what is fibonacci series?

#let me explain with example.. it is a type of series in which next term is the sum of previous two.

#e.g. 0 , 1 , 1 , 2 , 3 , 5 , 8 , 13 , 21...... [ 0+1 = 1 , 1+1 =2 , 2+1 =3 ]

#So use for loop to show this series.


num1 = 0 #it counts as 1st element
num2 = 1 #counts as 2nd
num3 = 0
r = int(input("Enter how many terms you want to show"))

for i in range(1,r+1):

 print(num1)
 num3 = num1+ num2
 num1 = num2
 num2 = num3
    
    #if you have habit of taking range from (1,r-2)
    #you must print num1 and num2 above the loop itself. num1,num2 = 0,1 and print the stuff
    # i have modified it so that it will print all of the program at once rather than using 2 prints