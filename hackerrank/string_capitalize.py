# alan savio => Alan Savio
# hello     world => Hello     World

def solve(s):
    a = list(s)
    b = []

    for i in range(0,len(a)):
        if i == 0 or a[i-1] == " ":
            b.append(a[i].capitalize())
        else:
            b.append(a[i])
    
    string = "".join(b)
    
    return string

print(solve("hello    world"))