from functools import reduce

def chk(no):
    if(no % 2 == 0):
        return no
    
def sqr(no):
    return no**2

def add(A, B):
    return A+B

def main():
    n = int(input("Enter number of elements: "))
    print("Enter the numbers: ")
    List = []
    for i in range(n):
        a = int(input())
        List.append(a) 
    print(List)

    FData = list(filter(chk, List))
    print("Data after filter is: ", FData)

    MData = list(map(sqr, FData))
    print("Data after map is: ", MData)

    RData = reduce(add, MData)
    print("Data after reduce is: ", RData)

if __name__ == "__main__":
    main()