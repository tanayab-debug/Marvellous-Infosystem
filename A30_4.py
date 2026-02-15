import os
import sys
import shutil

def checkFile(Filename1, Filename2):
    shutil.copyfile(Filename1, Filename2)

def main():
    checkFile(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()