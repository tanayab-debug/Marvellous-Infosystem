def fact(No):
    val = 1
    for i in range(1,No+1):
        val = val * i
    return val

def main():
    No = 0
    No = int(input("Enter the number: "))

    ret = fact(No)
    print("Factorial of number is: ", ret)

if __name__ == "__main__":
    main()