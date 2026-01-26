def chk(No):
    if (No > 0):
        print("Even Number")
    elif (No < 0):
        print("Odd Number")
    else:
        print("Zero")

def main():
    No = 0
    No = int(input("Enter the number: "))
    chk(No)

if __name__ == "__main__":
    main()