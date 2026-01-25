from functools import reduce

def Min(A,B):
    return min(A,B)

def main():
    Data = [11,34,56,78]
    print("The data is: ", Data)

    Rdata = reduce(Min, Data)
    print("The minimum value is: ", Rdata)

if __name__ == "__main__":
    main() 