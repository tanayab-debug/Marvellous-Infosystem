def Min(list):
    print("minimum of number is: ", min(list))

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

    Min(list)
        
if __name__ == "__main__":
    main()