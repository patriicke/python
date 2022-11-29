import os
f = open("./FILE HANDLING/main.txt", "a")
f.write("\nGender: Male")
f.close()


# Deleting a file

if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("The file does not exist")
