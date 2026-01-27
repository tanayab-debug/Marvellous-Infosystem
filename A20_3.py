import threading

def EvenList(List):
    sum = 0
    for no in List:
        if(no%2 == 0):
            sum += no
    print("Sum of even number is: ", sum)

def OddList(List):
    sum = 0
    for no in List:
        if(no%2 != 0):
            sum += no
    print("Sum of odd number is: ", sum)


def main():
    List = []
    no = 0
    no = int(input("Enter the number of elements: "))

    print("Enter elements: ")
    for i in range(no):
        a = int(input())
        List.append(a)
    print(List)

    t1= threading.Thread(target=EvenList, args=(List,))
    t2= threading.Thread(target=OddList, args=(List,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()