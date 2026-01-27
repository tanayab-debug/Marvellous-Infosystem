import threading

def chkprime(No):
    if No <= 1:
        return False

    for i in range(2, No):
        if No % i == 0:
            return False

    return True

def prime(List):
    List1 = []
    for no in List:
        a = chkprime(no)
        if (a == True):
            List1.append(no)
    print("The list of prime numbers is: ", List1)


def Notprime(List):
    List2 = []
    for no in List:
        a = chkprime(no)
        if (a != True):
            List2.append(no)
    print("The list of prime numbers is: ", List2)
    
def main():
    List = []
    no = 0
    no = int(input("Enter the number of elements: "))

    print("Enter elements: ")
    for i in range(no):
        a = int(input())
        List.append(a)
    print(List)

 
    t1= threading.Thread(target=prime, args=(List,))
    t2= threading.Thread(target=Notprime, args=(List,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()
