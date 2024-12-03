import os
import time
# creating a file that creates and deletes files

files = []

wD= os.getcwd() # getting the current working directory
def warn():
    print("!! remember to include the extensions")
    return None  
def loading():
    bootSymbol = '-'
    while True:
        bootSymbol += '-'


while True: 
    print("Create[c] or delete[d] files")
    userInput = input("-- ")
    if userInput == "c":
        # asking to write into the new file
        try: 
            warn()
            fileName = input("name of the file --")
            newFile = open(os.path.join(wD , "x"))
            print("this worked")
            writeCond = input("do you want to write into the newly created file[y/n]")
            if writeCond == "y":
                newText = input("--")
                newFile.write(newText)
            else:
                exit()
            newFile.close()
        except:
            print("File already Exists")
    elif userInput == "d":
        warn()
        print("What file do you want to delete in this directory")
        fileName = input("--")
        time.sleep()
        os.remove(fileName)



