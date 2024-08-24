# A scope of a variable is the region where the variable is recognized
# A variable is available inside the region it is created
# A global and local version of a variable can be created 

name = "Alan"               #global scope of the variable (available inside and outside the function)

def last_name():
    name = "Savio"           #local scope of the variable (only available inside this function)
    print(name)

print(name)  
last_name()              

