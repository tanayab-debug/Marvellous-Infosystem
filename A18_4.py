import MarvellousNum

def ListPrime(Data):
    Sum = 0

    for no in Data:
        if MarvellousNum.ChkPrime(no):
            Sum = Sum + no

    return Sum


def main():
    N = int(input("Enter number of elements: "))

    Arr = []

    print("Enter the elements:")
    for i in range(N):
        value = int(input())
        Arr.append(value)

    Result = ListPrime(Arr)
    print("Addition of prime numbers is:", Result)


if __name__ == "__main__":
    main()