from functools import reduce

def Add(A,B):
    return A+B

def main():
    Data = [11,34,56,78]
    print("The data is: ", Data)

    Rdata = reduce(Add, Data)
    print("The addition of data is: ", Rdata)

if __name__ == "__main__":
    main() 