import threading

def Num1():
    print("1 to 50: ")
    for i in range(1, 51):
        print(i)

def Num2():
    print("50 to 1: ")
    for i in range(50, 0, -1):
        print(i)


def main():

    t1= threading.Thread(target=Num1)
    t1.start()
    t1.join()

    t2= threading.Thread(target=Num2)
    t2.start()
    t2.join()

if __name__ == "__main__":
    main()