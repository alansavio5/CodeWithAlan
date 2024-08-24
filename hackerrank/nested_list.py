# print the name of students with second lowest grade

# input
#    5
#   Harry
#   37.21
#   Berry
#   37.21
#   Tina
#   37.2
#   Akriti
#   41
#   Harsh
#   39

# output
#   Berry
#   Harry

if __name__ == '__main__':
    new_list = []
    n = int(input())
    for i in range(n):
        a = []
        name = input()
        score = float(input())
        for j in range(2):
            a.append(name)
            a.append(score)
            break
        new_list.append(a)
    

    marks = lambda mark:mark[1]
    new_list.sort(key=marks)

    new_mark = list(map(lambda data:data[1],new_list))
    
# 5
# Harsh
# 20
# Beria
# 20
# Varun
# 19
# Kakunami
# 19
# Vikas
# 21