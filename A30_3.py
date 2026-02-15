import os
import sys
import shutil

def checkFile(Filename):
    fobj = open(Filename, "r") 
    ret = fobj.readlines()
    for line in ret:
        print(line)

def main():
    checkFile(sys.argv[1])

if __name__ == "__main__":
    main()