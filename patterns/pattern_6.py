n = int(input("Enter a number: "))

for i in range(n):
    for j in range(0,i+1):
        for k in range(0,j+1):
            print(j+1,end=" ")
            break
    i+=1
    print()
