from functools import reduce

def Max(A,B):
    return max(A,B)

def main():
    Data = [11,34,56,78]
    print("The data is: ", Data)

    Rdata = reduce(Max, Data)
    print("The maximum number is: ", Rdata)

if __name__ == "__main__":
    main() 