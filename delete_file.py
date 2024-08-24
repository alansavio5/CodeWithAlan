import os

path = "new.txt"

try:
    os.remove(path)

except FileNotFoundError:
    print("File not found")

except PermissionError:
    print("You have no permission to delete this file")

else:
    print(f"{path} was deleted")



















