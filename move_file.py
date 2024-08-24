import os

source = "new.txt"
destination = "C:\\Users\\Alan Savio\\OneDrive\\Desktop\\move.txt"

try:
    if os.path.exists(destination):
        print("There is already a file")
    else:
        os.replace(source,destination)
        print("File moved")

except FileNotFoundError:
    print(f"{source} not found")
