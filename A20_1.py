import threading

def even():
    print("First 10 even numbers are:")
    for i in range(2,20,2):
        print(i)

def odd():
    print("First 10 odd numbers are:")
    for i in range(1,20,2):
        print(i)

def main():

    t1=threading.Thread(target=even)
    t2=threading.Thread(target=odd)

    t1.start() 
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()  