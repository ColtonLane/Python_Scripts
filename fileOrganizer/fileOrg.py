import sys #used to read cmd arguments
import os #used to avoid inconsistency in different OS's path syntax and to obtain CWD
import json
import shutil
from subprocess import PIPE, run

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
    folderPath = os.path.join("{}\\{}".format(source, type))
    if os.path.isdir(folderPath) == False: #checks if a folder of name "type" exists; 
        os.makedirs(folderPath)
    for i in fileList: 
        shutil.move(i, folderPath)
    if len(os.listdir(folderPath)) == 0: 
        shutil.rmtree(folderPath)

def findAllFileTypes(source): 
    typeList = ["png", "jpg", "gif", "svg", "tiff", "tif", "docx", "doc", "html", "xlsx", "ppxt", "mp4", "avi", "MOV", "flv", "avchd", 
                "pptx", "odp", "key", "m4a", "mp3", "wav", "exe", "bat", "rtf", "aseprite", "jpeg", "txt", "pdf", "py", "java", "css", 
                "cs", "cpp", "iso", "aseprite-extension", "z64", "7z", "json", "zip", "sf2", "ipynb", "lss", "msi", "webp"]
    for i in typeList: 
        addToFolder(findFilesOfType(i, source), i, source)

def main(source, fileType): 
    cwd = os.getcwd()
    source_path = os.path.join(cwd, source)
    fileType.replace(".", "")

    if (fileType == "ALL"): 
        findAllFileTypes(source)
    else: 
        addToFolder(findFilesOfType(fileType, source_path), fileType, source)


if __name__ == "__main__": 
    args = sys.argv
    print(args)
    if len(args) != 3: 
        raise Exception("Only pass a source directory and desired file type to be sorted")
    
    source, fileType = args[1:]
    main(source, fileType)