a = [i for i in range(1,101) if i%2==0]
print(a)
print("\n")

n = 4
x = 2
y = 2
z = 2
b = [[i,j,k] for i in range(0,x+1) for j in range(0,y+1) for k in range(0,z+1) if (i+j+k)!=n]
print(b)

