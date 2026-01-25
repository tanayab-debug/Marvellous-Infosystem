def ChkOdd(No):
    if(No%2 != 0):
        return No

def main():
    Data = [11,34,56,78]
    print("The data is: ", Data)

    Fdata = list(filter(ChkOdd, Data))
    print("The odd numbers are: ", Fdata)

if __name__ == "__main__":
    main() 