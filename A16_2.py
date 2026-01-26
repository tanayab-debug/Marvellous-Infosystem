def ChkNum(No):
    if (No % 2 == 0):
        return "Even"
    else:
        return "Odd"

def main():
    No = 0
    No = int(input("Enter the number: "))
    Result = ChkNum(No)
    print("The number is: ", Result)

if __name__ == "__main__":
    main()