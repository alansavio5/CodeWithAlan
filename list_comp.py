squares = [i*i for i in range(1,11)]
print(squares)

# print the passed students (>=60) using filter function
students = [0,10,20,30,40,50,60,70,80,90,100]
passed_students = list(filter(lambda x:x >= 60,students))
print(passed_students)

# write the same program using list comprehensions
passed_studentss = [i for i in students if i >= 60]
print(passed_studentss)