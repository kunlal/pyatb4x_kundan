# Task 7
# Create a program that determines whether a given year is a leap year.
#
# A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.
#
# Use an if-else statement to make this determination.

# 1 year <100 and %4 ==  - leap year
# 2 year >100 and %400 == - leap year
# 3 year >100 and %4 ==0 and %100!= 00 == - leap year

year = int(input("Please enter a year\n: "))

if year < 100 and year % 4 == 0:
    print(f"{year} Leap Year: 1")
elif year > 100 and year % 400 == 0:
    print(f"{year} Leap Year: 3")
elif year > 100 and year % 100 != 0 and year % 4 == 0:
    print(f"{year} Leap Year: 3")
else:
    print(f"{year} Not a Leap Year: else")