def main():
    no = 0
    no = int(input("Enter the number: "))
    line=""
    for i in range(1,no+1):
        line = line + str(i)

    for i in range(no):
        print(line)  

if __name__ == "__main__":
    main()