student = ["Alan","Ajay","Sebin","Nibin","Nelson"]
student.sort()
for i in student:
    print(i)

print("*******************************")

student.sort(reverse=True)
for i in student:
    print(i)

print("*******************************")

students = ("Alan","Ajay","Sebin","Nibin","Nelson")
sorted_student = sorted(students)
for i in sorted_student:
    print(i)

print("*******************************")

sorted_student = sorted(students,reverse=True)
for i in sorted_student:
    print(i)

print("*******************************")

students_new = [("Soorej",48,67),
                ("Pranav",53,89),
                ("Vinay",61,77),
                ("Faheem",22,80)]

students_new.sort()
for i in students_new:
    print(i)

print("*******************************")

roll_no = lambda roll : roll[1]
student.sort(key=roll_no)
for i in students_new:
    print(i)

print("*******************************")

marks = lambda mark : mark [2]
students_new.sort(key=marks)
for i in students_new:
    print(i)
