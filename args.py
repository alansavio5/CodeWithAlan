#args >>>>>>>>>>>>> a parameter that packs all arguments into a tuple

def add(*args):         # function(*variable_name)
    sum = 0
    args = list(args)
    args[0] = 0         #setting the value at index 0 as 0
    for i in args:
        sum+=i
    return sum

print(add(1,2,3))
