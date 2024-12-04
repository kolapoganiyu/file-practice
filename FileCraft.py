import os
import time
from pathlib import Path
# creating a file that creates and deletes files

files = []

wD= str(os.path.dirname(__file__)) # getting the current working directory
print(wD)
def warn():
    print("!! remember to include the extensions")
    return None  
def loading():
    print("deleting")
    i = 0
    bootSymbol = '-'

    while i < 10:
        if i % 2 == 0:
            time.sleep(2)
        print(bootSymbol)
        bootSymbol += "-"
        i+=1


while True: 
    print("Create[c] or delete[d] files")
    userInput = input("--")
    if userInput == "c":
        # asking to write into the new file
        try: 
            warn()
            fileName = input("name of the file --")
            newFile = open(os.path.join(wD , fileName), "x")
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
        loading()
        if os.path.exists(os.path.join(wD, fileName)):  # checking if the file exists before the delete process
           os.remove(fileName)
        else:
            print("this file does not exist")