import os
from sys import *    

def Directory_Watcher(Dir_Name):
    print("Inside directory watcher method")
    print("Name of input directory : ",Dir_Name)
    
    flag = os.path.isabs(Dir_Name)
    if flag == False:
        Dir_Name = os.path.abspath(Dir_Name)
    else:
        return
    
    for folder_name, subfolder,Filenames in os.walk(Dir_Name):
        print(f"Folder name is : {folder_name} ")
        for subf in subfolder:
            print(f"Subfolder name of {folder_name} is {subf} ")
        for fnames in Filenames:
            print(f"File inside {folder_name} is {fnames} ")
            print(f"With size : {os.path.getsize(os.path.join(folder_name,fnames))}")
            print(" ")
                       
def main():
    print("Directory watcher application")
    
    if(len(argv) < 2):
        print("Insufficient arguments")
        exit()
    
    if(argv[1] == "-h"):
        print("This scrip will travel the directory and display the names of all entries")
        exit()
        
    if(argv[1] == "-u"):
        print("Usage : Application_name Directory_name")
        exit()
        
    try:
        Directory_Watcher(argv[1])

    except ValueError:
        print("Error : Invalid datatype of input")

    except Exception as e:
        print("Error : Invalid input",e)
        
if __name__ == "__main__":
    main()