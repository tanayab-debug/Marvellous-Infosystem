import threading

def Max(List):
    print("Maximum is: ", max(List))

def Min(List):
    print("Minimum is: ", min(List))

def main():
    List = []
    no = 0
    no = int(input("Enter the number of elements: "))

    print("Enter elements: ")
    for i in range(no):
        a = int(input())
        List.append(a)
    print(List)

    t1= threading.Thread(target=Max, args=(List,))
    t2= threading.Thread(target=Min, args=(List,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()
