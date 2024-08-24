from itertools import permutations

string,n = input().split()
lis = list(string)
print(list(permutations(lis,int(n))).sort(),end="\n")
