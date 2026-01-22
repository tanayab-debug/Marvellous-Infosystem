def mulTable(a):
    mul = []
    for i in range(1,11):
        t = a*i
        mul.append(t)
    return mul

def fact(a):
    sum = 0
    for i in range(a+1):
        sum = sum + i
    return sum

def even(a):
    list = []
    for i in range(2, a+1, 2):
        list.append(i)
    return list

def odd(a):
    list = []
    for i in range(1, a+1, 2):
        list.append(i)
    return list

def main():
    a = 0
    a = int(input("Enter 1st number: "))

    Table = mulTable(a)
    print(f"multiplication table of {a}: ", Table)

    factorial = fact(a)
    print(f"Factorial of {a}: ", factorial)

    EvenNo = even(a)
    print(f"even no till {a}: ", EvenNo)

    oddNo = odd(a)
    print(f"odd no till {a}: ", oddNo)

if __name__ == "__main__":
    main()