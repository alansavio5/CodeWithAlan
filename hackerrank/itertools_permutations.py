from itertools import permutations

string,num = input().split()
string = list(string)
string.sort()
result = list(permutations(string,int(num)))
for i in result:
    print("".join(list(i)))