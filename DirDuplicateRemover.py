from sys import *
import os
import hashlib
import time

def DeleteFiles(dict1):
    results = list(filter(lambda x:len(x) > 1, dict1.values()))
    
    iCnt = 0
    
    if len(results) > 0:
        for result in results:
            for subresult in result:
                iCnt+=1
                if iCnt >= 2:
                    os.remove(subresult)
            iCnt = 0
    else:
        print("No duplicate Files found")            

def hashfile(path, blocksize = 1024):
    fd = open(path, 'rb')
    hasher = hashlib.md5()
    buf = fd.read(blocksize)

    while len(buf) > 0:
        hasher.update(buf)
        buf = fd.read(blocksize)
    
    fd.close()
    
    return hasher.hexdigest()


def FindDuplicate(path):
    flag = os.path.isabs(path)
    
    if flag == False:
        path = os.path.abspath(path)
        
    exists = os.path.isdir(path)
    
    dups = {}
    if exists:
        for DirName, SubDirs, FileList in os.walk(path):
            print(f"Current folder is {DirName}")
            for filen in FileList:
                path = os.path.join(DirName,filen)
                file_hash = hashfile(path)
                if file_hash in dups:
                    dups[file_hash].append(path)
                else:
                    dups[file_hash] = [path]
        return dups
    else:
        print("Invalid path")
        

def PrintDuplicate(dict1):
    results = list(filter(lambda x: len(x) > 1, dict1.values()))
    
    if len(results) > 0:
        print("Duplicates Found :")
        print("The following files are duplicate ")
        iCnt = 0
        for result in results:
            for subresult in result:
                print('\t\t%s'%subresult)
    else:
        print("No duplicate files found")
        

def main():
    print(f"Application name : {argv[0]}")
    
    if(len(argv) != 2):
        print("Error : Invalid number of arguments")
        exit()
        
    if(argv[1] == "-h") or (argv[1] == "-H"):
        print("This Script is used to traverse specific directory and display sizes of files")
        exit()
        
    if(argv[1] == "-u") or (argv[1] == "-U"):
        print("usage : ApplicationName AbsolutePath_of_DirectoryExtension")
        exit()
            
    try:
        arr = {}
        start_time = time.time()
        arr = FindDuplicate(argv[1])
        PrintDuplicate(arr)
        DeleteFiles(arr)
        end_time = time.time()
        
        print(f"Took {end_time - start_time} seconds to evaluate")
        
    except ValueError:
        print("Error : Invalid datatype of input") 
        

if __name__ == "__main__":
    main()   