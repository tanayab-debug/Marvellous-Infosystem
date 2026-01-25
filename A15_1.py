def sqr(No):
    return No**2

def main():
    Data = [11,34,56,78]
    print("The data is: ", Data)

    Mdata = list(map(sqr, Data))
    print("The data after mapping is: ", Mdata)

if __name__ == "__main__":
    main()