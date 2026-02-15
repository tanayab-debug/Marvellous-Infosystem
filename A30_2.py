import os
import sys

def checkFile(Filename):
    fobj = open(Filename, "r") 
    ret = fobj.read()
    words = ret.split()
    return len(words)

def main():
    count = checkFile(sys.argv[1])
    print(count)

if __name__ == "__main__":
    main()