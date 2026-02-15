import os
import shutil

def make(Dir):
    if os.path.exists(Dir):
        files = os.listdir(Dir)
        os.mkdir("Temp")
        for file in files:
            shutil.copy2(os.path.join(Dir, file), "Temp")
    

def main():
    DirName = input("Enter the name of directory: ")
    make(DirName)

if __name__ == "__main__":
    main()