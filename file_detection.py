import os

path = input("Enter the path: ")

if os.path.exists(path):
    print("Item found")
    if os.path.isfile(path):
        print("It is a file")
    elif os.path.isdir(path):
        print("It is a directory")

else:
    print("Item not found")











