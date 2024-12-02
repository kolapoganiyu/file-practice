# creating a file that creates and deletes files

files = []

while True: 
    print("Create[c] or delete[d] files")
    userInput = input("-- ")
    if userInput == "c":
        print("!! remember to include the extensions")
        fileName = input("what is the name of the file you want to create -- ")
        try: 
            newFile = open(fileName , 'x')
            writeCond = input("do you want to write into the newly created file[y/n]")
            if writeCond == "y":
                newText = input("--")
                newFile.write(newText)
            newFile.close()
        except:
            print("File already Exists")
        

