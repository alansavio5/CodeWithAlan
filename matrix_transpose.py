a=[[1,1,1,1],
   [2,2,2,2],
   [3,3,3,3],
   [4,4,4,4]]

b=[[0,0,0,0],
   [0,0,0,0],
   [0,0,0,0],
   [0,0,0,0]]

for i in range(len(a)):
    for j in range(len(a[i])):
        b[j][i]=a[i][j]

for i in range(len(a)):
    for j in range(len(a[i])):
        print(b[i][j],end="\t")
    print()