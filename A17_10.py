def main():
    no = 0
    no = input("Enter the number: ")
    sum = 0
    for i in range(len(no)):
        sum = sum + int(no[i])
    print("Sum is: ", sum)

if __name__ == "__main__":
    main()