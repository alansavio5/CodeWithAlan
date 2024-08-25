from itertools import product

a = map(int,input().split())
b = map(int,input().split())

c = list(product(a,b))

for i in c:
    print(i,end=" ")