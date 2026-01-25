square = lambda a : a*a
cube = lambda a : a**3
maximum = lambda no1, no2: max(no1, no2)
minimum = lambda no1, no2: min(no1, no2)
value = lambda no1: (no1%2 == 0)
value2 = lambda no1: (no1%5 == 0)
add = lambda no1, no2: no1+no2
mul = lambda no1,no2: no1*no2
largest = lambda no1,no2,no3 : max(no1,no2,no3)

def main():
    a = int(input("enter number1: "))
    b = int(input("enter number2: "))
    c = int(input("enter number3: "))
    print("The square of number is: ", square(a))
    print("The cube of number is: ", cube(a))
    print("The maximum number is: ",maximum(a,b))
    print("The minimum number is: ",minimum(a,b))

    if value(a) == True:
        print(f"{a} is even")
    else:
        print("{a} is odd")

    if value2(a) == True:
        print(f"{a} is divisible by 5")
    else:
        print("{a} is not divisible by 5")

    print("The addition of numbers is: ", add(a,b))
    print("The multiplication of number is: ", mul(a,b))
    print("The maximum number is: ",largest(a,b,c))

if __name__ == "__main__":
    main()