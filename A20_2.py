import threading
#1,2,4,5,10
def evenfactor(no):
    sum=0
    for i in range(1,no+1):
        if(no%i==0 and i%2 ==0):
            sum = sum+i

    print("Sum of even factors is: ", sum)   

def oddfactor(no):
    sum=0
    for i in range(1,no+1):
        if(no%i==0 and i%2 !=0):
            sum = sum+i

    print("Sum of odd factors is: ", sum)

def main():

    t1=threading.Thread(target=evenfactor, args=(20,))
    t2=threading.Thread(target=oddfactor, args=(20,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()  