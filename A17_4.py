def SumFact(no):
    sum = 0
    for i in range(1,no):
        if(no%i == 0):
            print(i)
            sum = sum + i
    return sum


def main():
    no = 0
    no = int(input("Enter the number: "))
    ret = SumFact(no)
    print("sum of Factorials of number is: ", ret)    

if __name__ == "__main__":
    main()