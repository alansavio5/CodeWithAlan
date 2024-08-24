# filter() = creates a collection of elements from an iterable for which a function returns true
# syntax >>>> filter(function,iterble)

friends = [("Hari",16),
            ("Sia",17),
            ("jeswin",19),
            ("Asif",20),
            ("Raechel",18)]

age = lambda data : data[1]>=18

new_friends=list(filter(age,friends))

for i in new_friends:
    print(i)
