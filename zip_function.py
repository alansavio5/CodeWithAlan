# zip function >>>>>>>>> aggregate elements from two or more iterables (list, tuple, set, etc)
#                           create a zip object with paired stored in tuples for each elements

names = ["Luffy","Zoro","Sanji"]
passwords = ("password","1234","hbj#5")
users = dict(zip(names,passwords))

for key,value in users.items():
    print(f"{key} : {value}")

name = ["Nami","Ussop","Chopper"]
password = ("$$1000$$","sogeking#007","cotton candy")
last_login = ["2 days ago","7 hrs ago","1 month ago"]
user = zip(name,password,last_login)

for x in user:
    print(x)