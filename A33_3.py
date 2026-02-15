import sys
import os
import time
import schedule
import psutil

def Monitoring(Filename):

    fobj = open(Filename, "a")

    for process in psutil.process_iter():
        Name = process.name()
        PID = process.pid
        threads = process.num_threads()
        timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
        CPU_USAGE = psutil.cpu_percent()
        mem = psutil.virtual_memory()
        for part in psutil.disk_partitions():
            usage = psutil.disk_usage(part.mountpoint)


        fobj.write("%s | Process %s | PID %s | Threads %s | CPU Usage: %s | RAM Used: %s | %s : %s %% \n" %(timestamp, Name, PID, threads, CPU_USAGE, mem.percent, part.mountpoint, usage.percent))

        try:
            open_files = process.open_files()
            num_files = len(open_files)
            fobj.write("The number of open files in this process are: %s\n" %(num_files))

        except(psutil.AccessDenied, psutil.NoSuchProcess):
            pass
        
def max_mem(Filename):
    Monitoring(Filename)
    processes = []

    for proc in psutil.process_iter(['pid','name','memory_info']):
        mem = proc.info['memory_info'].rss/(1024*1024)

        processes.append({
            'pid' : proc.info['pid'],
            'name' : proc.info['name'],
            'mem_mb' : mem
        })

    processes = sorted(processes, key=lambda x: x["mem_mb"], reverse=True)
    print("Top 10 Memory Consuming Processes:\n")
    for process in processes[:10]:
        print(f"PID: {process['pid']:<8} "
            f"Name: {process['name']:<25} "
            f"Memory: {process['mem_mb']:.2f}%")



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

    #python Demo.py 5 Data
    elif(len(sys.argv) == 3):
        print("Inside projects logic")
        print("Time interval: ", sys.argv[1])
        print("Directory name: ", sys.argv[2])
        
        #Apply the scheduler
        schedule.every(int(sys.argv[1])).minutes.do(max_mem, sys.argv[2])

        print("Data Field System started successfully")
        print("Time Interval in minutes: ", sys.argv[1])
        print("Press ctrl C to stop the execution")

        #wait till abort
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