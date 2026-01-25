from functools import reduce

def product(A,B):
    return (A*B)

def main():
    Data = [11,34,56,78]
    print("The data is: ", Data)

    Rdata = reduce(product, Data)
    print("The multiplication of all numbers is: ", Rdata)

if __name__ == "__main__":
    main() 