import os
import shutil

folder = "folder"

try:
    #os.rmdir(folder)               #delete an empty folder
    shutil.rmtree(folder)           #delete a folder and all files within that folder

except FileNotFoundError:
    print("Folder not found")

except PermissionError:
    print("You don't have permission to delete this folder")

except OSError:
    print("You cannot delete an empty folder using that function")

else:
    print(f"{folder} wass deleted")



















