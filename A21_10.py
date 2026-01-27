import threading

def sum(List):
    sum = 0
    for no in List:
        sum = sum + no
    print("Summation of all numbers is: ", sum)

def mul(List):
    sum = 1
    for no in List:
        sum = sum * no
    print("Multiplition of all numbers is: ", sum)

def main():
    List = []
    no = 0
    no = int(input("Enter the number of elements: "))

    print("Enter elements: ")
    for i in range(no):
        a = int(input())
        List.append(a)
    print(List)

    t1= threading.Thread(target=sum, args=(List,))
    t2= threading.Thread(target=mul, args=(List,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    

if __name__ == "__main__":
    main()
