nterms = int(input("Enter the number of terms: "))
n1 = 0
n2 = 1
count = 0

if nterms < 0:
    print("Enter a positive numer")

elif nterms == 1:
    print(f"Fibonacci series upto {nterms}:\n1")

else:
    print(f"Fibonacci series upto {nterms}:")
    while count < nterms:
        if count != nterms:
            print(f"{n1}, ",end="")
        else:
            print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
