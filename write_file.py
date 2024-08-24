text = "Hello there\nHave a nice day!!!"

with open("test.txt","w") as file:                  # "w" for write 
    file.write(text)


new_text = "\nGood Bye"

with open("test.txt","a") as file:                  # "a" for append
    file.write(new_text)


with open("test.txt","r") as file:                  #"r" for read
    print(file.read())











