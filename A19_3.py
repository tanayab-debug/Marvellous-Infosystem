from functools import reduce

def chk(no):
    if(no >= 70 or no <=90):
        return no
    
def increment(no):
    return no+10

def product(A, B):
    return A*B

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

    MData = list(map(increment, FData))
    print("Data after map is: ", MData)

    RData = reduce(product, MData)
    print("Data after reduce is: ", RData)

if __name__ == "__main__":
    main()