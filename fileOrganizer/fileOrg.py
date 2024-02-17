import sys #used to read cmd argumentsfilesMoved
import os #used to avoid inconsistency in different OS's path syntax and to obtain CWD
import shutil

global filesMoved 
filesMoved = 0
global foldersMade
foldersMade = 0

def findFilesOfType(type, source): 
    fileList = []
    for root, dirs, files in os.walk(source): 
        for file in files: 
            if file.endswith(".{}".format(type)) or file.endswith(".{}".format(type.upper())) or file.endswith(".{}".format(type.lower())): #checks if string ends in "." followed by specified path (avoids replacing none-type periods by mistake)
                curPath = os.path.join(source, file) #combines source directory and files ending in given type
                fileList.append(curPath)
        break 
    return fileList 

def addToFolder(fileList, type, source): 
    global filesMoved, foldersMade
    folderPath = os.path.join("{}\\{}".format(source, type))
    if os.path.isdir(folderPath) == False: #checks if a folder of name "type" exists; 
        os.makedirs(folderPath)
        foldersMade += 1

    for file in fileList: 
        filePath = os.path.join("{}\\{}".format(folderPath, os.path.basename(file))) #creates filePath to check if file exists in folder
        if os.path.isfile(filePath) == False: #checks is file of the same name exists; if not, adds file to folder
            shutil.move(file, folderPath)
            filesMoved += 1

def findAllFileTypes(source): 
    typeList = []
    for root, dirs, files, in os.walk(source): 
        for file in files: 
            curFType = file[file.rfind(".")+1::]
            if curFType not in typeList: 
                typeList.append(curFType)
        break
    print("Organizing files of type(s): {}".format(typeList))

    for type in typeList: 
         addToFolder(findFilesOfType(type, source), type, source)

def main(source, fileType): 
    source_path = os.path.join(os.getcwd(), source)
    print("\n")
    fileType.replace(".", "")

    if (fileType == "ALL"): 
        findAllFileTypes(source)
    else: 
        addToFolder(findFilesOfType(fileType, source_path), fileType, source)

    print("Created {} folders \nMoved {} files".format(foldersMade, filesMoved))


if __name__ == "__main__": 
    args = sys.argv
    print(args)
    if len(args) != 3: 
        raise Exception("Only pass a source directory and desired file type to be sorted")
    
    source, fileType = args[1:]
    main(source, fileType)