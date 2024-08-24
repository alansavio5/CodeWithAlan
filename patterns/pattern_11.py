#                G
#              GR
#            GRA
#          GRAM
#        GRAMP
#      GRAMPR
#    GRAMPRO

string = "PROGRAM"
start = []
end = []
length = len(list(string))
mid = length/2

for i in range(length):
    if i<mid-1:
        start.append(string[i])
    else:
        end.append(string[i])

end.extend(start)

for x in range(length):
    for y in range(length-1-x):
        print("   ",end="")
    for z in range(x+1):
        print(end[z],end="")
    print()
