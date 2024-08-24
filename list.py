month = ["January","February","March"]

print(month[2])

print("\n")

month[2] = "April"          #change an element from the list

print(month[2])

print("\n")

for x in month:
    print(x)

print("\n")

month.append("May")         #append an element at the end

for x in month:
    print(x)

print("\n")

month.remove("February")    #remove a certain element       

for x in month:
    print(x)

print("\n")

month.pop()                 #remove the last element

for x in month:
    print(x)

print("\n")

month.insert(0,"December")  #add an element at the given index

for x in month:
    print(x)

print("\n")

month.sort()                #sort the list alphabetically

for x in month:
    print(x)

print("\n")

month.reverse()             #reverse the list

for x in month:
    print(x)

print("\n")

month.clear()               #remove all elements from the list
