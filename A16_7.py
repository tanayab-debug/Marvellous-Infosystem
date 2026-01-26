def ChkNum(No):
    if (No % 5 == 0):
        return True
    else:
        return False

def main():
    No = 0
    No = int(input("Enter the number: "))
    Result = ChkNum(No)
    print(Result)

if __name__ == "__main__":
    main()