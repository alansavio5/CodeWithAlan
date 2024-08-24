def fib(n):
    if n < 0:
        print("Enter a positive integer")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
        
n=int(input("Enter a number: "))
fib(n)
print(f"Fiboacci number at {n} is {fib(n)}")