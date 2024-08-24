#copyfile() >>>>>> copy the content of a file
#copy() >>>>>> copyfile() + permission mode + destination can be a directory
#copy2() >>>>>> copy() + copies metedata (file's creation and modification time)

import shutil

shutil.copyfile("new.txt","copy.txt")               # copyfile(source,destination)
































