# leap year

year = int(input("Enter any year: "))
new_year = year/4
leap_year = year//4
if new_year == leap_year:
    print("Leap Year")
else:
    print("Not leap year")
