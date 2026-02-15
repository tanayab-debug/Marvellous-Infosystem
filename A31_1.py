import os

def check(Filename):
    #if os.path.exists(Filename):
    name, ext = os.path.splitext(Filename)
    if ext == ".txt":
        print(Filename)

def main():
    num = int(input("Enter the number of files."))
    names = []
    i=0
    while (i<num):
        fname = input("Enter the name of file: ")
        names.append(fname)
        i+=1

    for i in names:
        check(i)

if __name__ == "__main__":
    main()