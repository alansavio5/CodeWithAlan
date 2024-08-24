# input = PROGRAM
# output 
#       
#                G
#              GR
#            GRA
#          GRAM
#        GRAMP
#      GRAMPR
#    GRAMPRO

string = input("Enter the string: ")
a = list(string)
mid = len(a)//2
b=[]                    # [p,r,o]
c=[]                    # [g,r,a,m]
space = len(string)
for i in range(len(a)):
    if i<mid:
        b.append(a[i])
    else:
        c.append(a[i])

for j in range(len(string)):
    for k in range(space):
        print(end="  ")
    space -= 1
    for l in range(space-1):
        pass