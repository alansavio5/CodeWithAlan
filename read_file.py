try:
    with open("test.txt","r") as file:              # "r" for read, "w" for write, "a" for append
        print(file.read())

except FileNotFoundError:
    print("File not found")

else:
    print(file.closed)              # When we read a file using 'open' it always close the file after reading >>>> it will return true
