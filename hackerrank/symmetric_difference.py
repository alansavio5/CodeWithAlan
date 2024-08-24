# input
#       4
#       2 4 5 9
#       4
#       2 4 11 12

# output
#       5
#       9
#       11
#       12

s_one = int(input())
set_one = set(input().split())

s_two = int(input())
set_two = set(input().split())

diff1 = set(set_one.difference(set_two))
diff2 = set(set_two.difference(set_one))

a = list(sorted(diff1.union(diff2)))

result = [int(i) for i in a]
result.sort()
for j in result:
    print(j)