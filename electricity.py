unit = int(input("Enter the number of units: "))

if unit <= 100:
    print("No charge")

elif unit > 100 and unit <= 200:
    unit = unit - 100
    charge = unit * 5
    print(f"{charge} rs has to be paid")

else:
    unit = unit - 200
    charge = (unit * 10) + 500
    print(f"{charge} rs has to be paid")


