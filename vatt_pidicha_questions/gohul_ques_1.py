string = "Python is a programming language"
lis = []
lis = string.split(" ")

max_len = lis[0]
for i in range(1,len(lis)):
    if len(lis[i]) > len(max_len):
        max_len = lis[i]

print("{} has {} length".format(max_len,len(max_len)))
