# 1       5
#   2   4
#     3
#   2   4
# 5       5

for i in range(1,6):
    for j in range(1,6):
        if i==j or i+j==6:
            print(j,end=" ")
        else:
            print("",end=" ")
    print()
