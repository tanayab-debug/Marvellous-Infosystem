import os
import sys

def checkFile(Filename):
    fobj = open(Filename, "r") 
    ret = fobj.readline()
    cnt = 0
    for ret in fobj:
        cnt +=1
    return cnt

def main():
    count = checkFile(sys.argv[1])
    print(count)


if __name__ == "__main__":
    main()