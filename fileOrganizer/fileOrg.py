import sys #used to read cmd arguments
import os #used to avoid inconsistency in different OS's path syntax and to obtain CWD
import json
import shutil
from subprocess import PIPE, run

def findFilesOfType(type, source): 
    file_paths = []

    for root, dirs, files in os.walk(source): 
        for directory in dirs: 
            if directory.endswith(".{}".format(type)): #checks if string ends in "." followed by specified path (avoids replacing none-type periods by mistake)
                curPath = os.path.join(source, directory) #combines source directory and files ending in given type
                file_paths.append(curPath) 
        break 
    return file_paths

def createFileFolder(source, file_paths): 
    pass

def main(source, fileType): 
    cwd = os.getcwd()
    source_path = os.path.join(cwd, source)
    fileType.replace(".", "")
    file_paths = findFilesOfType(fileType, source_path)

    if file_paths == None: 
        print("No files of type '{}' found.".format(fileType))

if __name__ == "__main__": 
    args = sys.argv
    print(args)
    if len(args) > 3: 
        raise Exception("Only pass a source directory and desired file type to be sorted")
    
    source, fileType = args[1:]
    main(source, fileType)