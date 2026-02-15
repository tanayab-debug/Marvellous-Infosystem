import os
import hashlib

def checksum(Filename):
    hobj = hashlib.md5()

    fobj = open(Filename, "rb")
    Buffer = fobj.read(1024)
    while(len(Buffer)>0):
        hobj.update(Buffer)
        Buffer = fobj.read(1024)

    fobj.close()

    return hobj.hexdigest()

def directory(DirName):

    if (os.path.exists(DirName)):
        if(os.path.isdir(DirName)):

            all = {}
            fobj = open("Log.log", "a")
            for folderName, SubFolderName, FileName in os.walk(DirName):
                for fname in FileName:
                    Checksum = checksum(os.path.join(folderName, fname))
                    
                    if(Checksum in all):
                        fobj.write(os.path.join(folderName, fname)+"\n")
                    else:
                        all[Checksum] = [fname]

            fobj.close()
            print(all)
        
def main():
    DirName = input("Enter name of directory: ")
    directory(DirName)

if __name__ == "__main__":
    main()