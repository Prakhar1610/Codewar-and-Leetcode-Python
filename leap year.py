year = int(input("Enter the year: "))

if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
    print("{} is a leap year".format(year))
else:
    print("{} is not a leap year".format(year))