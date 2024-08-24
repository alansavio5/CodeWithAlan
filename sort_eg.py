person = [("Jacob",35,"Germany",12000),
          ("Kesav",23,"India",14000),
          ("Rafeeque",31,"UAE",11000),
            ("Lisa",28,"Russia",13000)]



# Q1)
#       Sort the list according to the name of each person

# Q2) 
#       Sort the list according to the age of each person
# 
# Q3)
#       Sort the list according to the country each of them live in
# 
# Q4)
#       Sort the list according to the salary of each person
      




names = lambda name : name[0]
person.sort(key=names)
for i in person:
    print(i)

print("______________________________")

ages = lambda age : age[1]
person.sort(key=ages)
for i in person:
    print(i)

print("______________________________")

countries = lambda country : country[2]
person.sort(key=countries)
for i in person:
    print(i)

print("______________________________")

salaries = lambda salary : salary[3]
person.sort(key=salaries)
for i in person:
    print(i)

