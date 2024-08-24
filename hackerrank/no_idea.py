# input
#   3 2
#   1 5 3
#   3 1
#   5 7

# output
#   1

happiness = 0

n,m = input().split()
set_new = set(input().split())
set_a = set(input().split())
set_b = set(input().split())

for i in list(set_new):
    if i in set_a:
        happiness += 1
    elif i in set_b:
        happiness -= 1

print(happiness)