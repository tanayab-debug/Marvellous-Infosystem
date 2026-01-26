def main():
    no = 0
    no = int(input("Enter the numberof elements: "))
    list = []
    sum = 0
    print("Enter numbers: ")
    for i in range(no):
        n = int(input())
        list.append(n)
    print(list)

    for i in range(len(list)):
        sum = sum + list[i]
    print("Sum of number is: ", sum)

        
if __name__ == "__main__":
    main()