while True:
    name = input("Enter your name: ")
    if name != "":
        break           #terminate the loop


phone_number = "123-4567-890"
for i in phone_number:
    if i == "-":
        continue        #skips the next iteration
    print(i,end="")
print("\n")


for i in range(1,21):
    if i % 2 == 1:
        pass            #do nothing, acts as a place holder
    else:
        print(i)








