year = int(input("Please:Enter the year you want to check"))

if (year % 4 == 0 and year%100 !=0 ):
    print("The year {} is a leap year".format(year))
elif (year % 100 == 0 and year%400==0 ):
        print("The year {} is a leap year".format(year))
else:
      print("It is not a leap year")


