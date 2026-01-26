from functools import reduce

def prime(no):
    for i in range(2, no+1):
        if(no%i == 0):
            return None
        return no
    
def mul(no):
    return no*2

def Max(A, B):
    return max(A,B)

def main():
    n = int(input("Enter number of elements: "))
    print("Enter the numbers: ")
    List = []
    for i in range(n):
        a = int(input())
        List.append(a) 
    print(List)

    FData = list(filter(prime, List))
    print("Data after filter is: ", FData)

    MData = list(map(mul, FData))
    print("Data after map is: ", MData)

    RData = reduce(Max, MData)
    print("Data after reduce is: ", RData)

if __name__ == "__main__":
    main()