# 3                     number of operations
# 10  5                 2
# 2   0                 ZeroDivisionError
# 8   @                 ValueError

num = int(input())
for x in range(num):
    try:
        lis = input().split()
        a = int(lis[0])
        b = int(lis[1])
        result = a/b
        if a % b == 0:
            print(int(result))
        else: 
            print("{:.2f}".format(result))
    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")
    except ValueError as e:
        print("Error Code:",e)
