import hashlib
import os
import shutil
import time
import zipfile
import sys
import schedule
import smtplib
from email.message import EmailMessage

def hash_val(path):
    hobj = hashlib.md5()
    fobj = open(path, "rb")

    while True:
        data = fobj.read(1024)
        if(len(data) > 1):
            hobj.update(data)
        else:
            break
    fobj.close()

    return hobj.hexdigest()

def Backup(Source, Destination):
    Copied_files = []

    os.makedirs(Destination, exist_ok=True)

    for root, dir, files in os.walk(Source):
        for file in files:
            src_path = os.path.join(root, file)

            relative = os.path.relpath(src_path,Source)

            des_path = os.path.join(Destination, relative)
            
            os.makedirs(os.path.dirname(des_path), exist_ok=True)

            if(not os.path.exists(des_path) or (hash_val(src_path) != hash_val(des_path))):
                shutil.copy2(src_path, des_path)
                Copied_files.append(relative)

    return Copied_files

def make_zip(folder):
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")

    zip_name = folder + "_" + timestamp + ".zip"
    zobj = zipfile.ZipFile(zip_name, "w", zipfile.ZIP_DEFLATED)

    for root, dir, files in os.walk(folder):
        for file in files:
            fpath = os.path.join(root, file)
            rpath = os.path.relpath(fpath, folder)

            zobj.write(fpath, rpath)

    zobj.close()
    return zip_name

def send_mail(zip_file, Log_file):
    sender = "a27267109@gmail.com"
    reciever = "bhoreptanaya@gmail.com"
    pswd = "oaygstdluszlqcen"
    sub = "Backup Files Report"

    msg = EmailMessage()
    msg['From'] = sender
    msg['To'] = reciever
    msg['Subject'] = sub

    msg.set_content("""
    Backup completed successfully
                    
    Attached Files:
        1.Zip File
        2.Log File
                    """)

    with open(zip_file, "rb") as f:
        msg.add_attachment(f.read(), maintype = "application", subtype  = "zip", filename = zip_file)

    with open(Log_file, "rb") as f:
        msg.add_attachment(f.read(), maintype = "txt", subtype  = "plain", filename = Log_file)

    smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    smtp.login(sender, pswd)
    smtp.send_message(msg)
    smtp.quit()

def restore_backup(zip_file, destination):
    if not os.path.exists(zip_file):
        print("Zip file not found!")
        return

    os.makedirs(destination, exist_ok=True)

    with zipfile.ZipFile(zip_file, "r") as z:
        z.extractall(destination)

    print("Backup restored successfully to:", destination)

def DataShield(Source, Destination):
    print("Backup process started at: ", time.ctime())
    timestamp = time.ctime()
    BackupName = Destination

    data = Backup(Source, BackupName)
    zip_file = make_zip(BackupName)
    Log_File = "Log.txt"

    fobj = open("Log.txt", "a")
    fobj.write("Copied Files are: \n %s" %data)
    fobj.write("Zip folder name is: \n %s" %zip_file)
    fobj.write("Backup started at: \n %s" %timestamp)
    fobj.close()
    send_mail(zip_file, Log_File)
    restore_backup(zip_file, BackupName)
    print("Files copied: ", len(data))
    print("Zip Files gets created: ", zip_file)

def main():

    Border = "-" * 50
    print(Border)
    print("----------Marvellous Data Sheild System-----------")
    print(Border)

    if(len(sys.argv)==2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This script is used to: ")
            print("1: Takes auto backup at given time")
            print("2: Backup only new and updated files")
            print("3: Create an archive of the backup periodically")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the automation script as")
            print("ScriptName.py TimeInterval SourceDirectory")
            print("TimeInterval: The time in minutes for periodic scheduling")
            print("SourceDirectory: Name of Directory to Backup")

        else:
            print("Unable to proceed as there is no such option")
            print("Please use --u or --h for details")

    elif(len(sys.argv) == 5 and sys.argv[4] == "--restore"):
        print("Inside projects logic")
        print("Time interval: ", sys.argv[1])
        print("Directory name: ", sys.argv[2])
        print("BackupFolder name: ", sys.argv[3])
        
        schedule.every(int(sys.argv[1])).minutes.do(DataShield, sys.argv[2],sys.argv[3])

        print("Data Field System started successfully")
        print("Time Interval in minutes: ", sys.argv[1])
        print("Press ctrl C to stop the execution")

        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid number of command line arguments")
        print("Unable to proceed as there is no such option")
        print("Please use --u or --h for details")

    print(Border)
    print("----------Thank you for using our Script----------")
    print(Border)


if __name__ == "__main__":
    main()