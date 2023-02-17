# ------------------------------------------------------------------------------------------------------
#                            How To Read The Files
# ------------------------------------------------------------------------------------------------------

f = open("mymodule.py", "r")

# Read First Two  Lines
print(f.readline())
print(f.readline())

# You can read all the file, line  by line
for x in f:
    print(x)

# close file
f.close()

# ------------------------------------------------------------------------------------------------------
#                            How To Write The Files
# ------------------------------------------------------------------------------------------------------

f1 = open("RegEx.py", "a")
f1.write("\n Now the file has more content")
f1.close()

f1 = open("RegEx.py", "r")
print(f1.read())
f1.close()



# ------------------------------------------------------------------------------------------------------
#                            How To Create The Files
# ------------------------------------------------------------------------------------------------------

f2 = open("myfile.py", "x")
f2 = open("myfile.py", "w")
f2.write("This file is new created through file handling ")
f2.read()


# ------------------------------------------------------------------------------------------------------
#                            How To Delete The Files
# ------------------------------------------------------------------------------------------------------

import os
os.remove("myfile.py")

import os
if os.path.exists("myfile.py"):
    os.remove("myfile.py")
else:
    print("The File Does not Exist")