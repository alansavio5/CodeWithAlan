from datetime import date

class Person:

    def __init__(self,name,country,dob):
        self.name = name
        self.country = country
        self.dob = dob

    def age(self):
        today = date.today()
        age = today.year - self.dob.year
        if today < date(today.year,self.dob.month,self.dob.day):
            age = age-1
        return age

person1 = Person("Alan","India",date(2001,11,13))
person2 = Person("Pranav","India",date(2002,5,25))

print(f"Name: {person1.name}")
print(f"Country: {person1.country}")
print(f"Age: {person1.age()}")
