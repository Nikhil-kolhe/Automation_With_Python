"""
   2. Write a program which accept file name from user and open that file and display the contents
    of that file on screen.
    Input : Demo.txt
    Display contents of Demo.txt on console.

"""

import os

def DirOpen(FileName):
    FileName = os.path.abspath(FileName)
    Path = os.getcwd()
   
    
    for FileNames in os.walk(Path):    
        if os.path.exists(FileName):
            os.system(FileName)
        else:
            print("There is No such a directory")
            return
            

def main():
    fname = input("Enter the file name : ")
    
    DirOpen(fname)

if __name__ == "__main__":
    main()