def main():
    no = 0
    no = int(input("Enter the number: "))

    for i in range(1,no+1):
        line = ""
        for j in range(1,i+1):
            line = line +str(j)
        print(line)

if __name__ == "__main__":
    main()