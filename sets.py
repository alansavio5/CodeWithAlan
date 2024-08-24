#sets  >>>>>>>>  collection of elements which unordered, unindexed, and no duplicate values

kitchen = {"knife","fork","spoon"}
for x in kitchen:
    print(x)
print()

#it may print the elements in differrent order in each step
#it is mainly used to check whether the set contains a certain elements
#faster than list

kitchen = {"knife","fork","spoon","spoon","spoon"}              #print spoon only 1 time
for x in kitchen:
    print(x)
print()

kitchen.add("napkin")                                           #add an element

for x in kitchen:
    print(x)
print()

kitchen.remove("spoon")                                         #remove an element

for x in kitchen:
    print(x)
print()

dishes = {"bowl","plate","cup"}

for x in dishes:
    print(x)
print()

kitchen.update(dishes)                                          #add one set to another (dishes -->> kitchen)

for x in kitchen:
    print(x)
print()

dishes.update(kitchen)                                          #add one set to another (kitchen -->> dishes)

for x in dishes:
    print(x)
print()

dinner_table = kitchen.union(dishes)                             #combine two sets to form a new set

for x in dinner_table:
    print(x)
print()

print(kitchen.intersection(dinner_table))
kitchen.s
