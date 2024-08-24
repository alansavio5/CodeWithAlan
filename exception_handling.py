# exception >>>>>>>>>>>>>>> events detected during execution which interrupts the flow of a program
try:
    numerator = int(input("Enter the number to divide: "))
    denominator = int(input("Enter the number to divide by: "))
    result = numerator/denominator                              

except ZeroDivisionError:
    print("Cannot divided by zero")             # When we divide by 0 there will occur a ZeroDivisionError

except ValueError:                              # When we enter a string other than numbers
    print("Enter only numbers")

else:
        print(result) 

finally:
    print("Thank You")                          # This block will always execute
