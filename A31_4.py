import os
import shutil

def make(Dir, New, Ext):
    if os.path.exists(Dir):
        files = os.listdir(Dir)
        os.mkdir(New)
        for file in files:
            name, ext = os.path.splitext(file)
            if ext == Ext:
                shutil.copy2(os.path.join(Dir, file), New)
    
def main():
    DirName = input("Enter the name of directory: ")
    NewDir = input("Enter the name of new directory: ")
    Ext = input("Enter the extension")
    make(DirName, NewDir, Ext)

if __name__ == "__main__":
    main()