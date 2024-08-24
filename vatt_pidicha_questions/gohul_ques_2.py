string = input("Enter the first string: ")
string_new = input("Enter the second string: ")
string = list(string)
string_new = list(string_new)
new_string = []

for i in string_new:
    for j in string:
        if i == j:
            new_string.append(j)
            break
        else:
            continue

if new_string == string_new:
    print("The string is anagram")
else:
    print("The string is not anagram")
