n = int(input("Enter any number: "))

def pattern(n):
    for i in range(0,n):
        for j in range(i+1):
            print("* ",end="")
        print("\n")
        
pattern(n)
