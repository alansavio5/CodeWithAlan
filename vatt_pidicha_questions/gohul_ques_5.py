# Find the occurrence of each character in a string without counting spaces.
# Do not use set and must not contain duplicates

string = input("Enter the string: ").lower()
a = [i for i in string if i!=" "]
b = []

for y in a:
    if y not in b:
        b.append(y)

for z in b:
    print(f"{z} = {a.count(z)}")
