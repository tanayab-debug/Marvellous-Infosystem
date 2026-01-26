def Add(A, B):
    return A + B

def main():
    No1 = int(input("Enter 1st number: "))
    No2 = int(input("Enter 2nd number: "))
    Result = Add(No1, No2)
    print("Addition of 2 numbers is: ", Result)

if __name__ == "__main__":
    main()