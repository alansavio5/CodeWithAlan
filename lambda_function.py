# Lambda functions can have any number of arguments, but they can only have one expression.
# Their syntax is restricted to a single line of code.

double = lambda x:x*2
print(double(5))

multiply = lambda x,y:x*y
print(multiply(5,5))

add = lambda x,y,z:x+y+z
print(add(1,2,3))

full_name = lambda f_name,l_name : f_name+l_name
print(full_name("Alan ","Savio"))

check_age = lambda age : True if age >= 18 else False
print(check_age(16))

