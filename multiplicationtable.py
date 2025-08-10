#WA Python program to display the multiplication table 

#Python program that displays the multiplication table of variable num e.g. show multiplication table of 12. Also print it in the format of 1  X 2 = 2 like this.

num = int(input("Please:Enter the number you want to show the multiplication table of "))
value =1

for i in range(1,11):#why not 10? because if we go upto 11, it will take upto 10. if we go upto 10 , it will take 9.
    value = num * i
    print("{} X {} is {} ".format(num,i,value))

