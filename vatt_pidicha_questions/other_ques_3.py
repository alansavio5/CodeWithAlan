# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.
# Example
# Let us assume the following comma separated input sequence is given to the program:
# 100,150,180
# The output of the program should be:
# 18,22,24

d = input("Enter the numbers: ")
c = 50
h = 30
q = []
list_new = d.split(",")

for i in list_new:
    q.append(str(round((2*c*int(i)/h)**0.5)))

print(",".join(q))
    