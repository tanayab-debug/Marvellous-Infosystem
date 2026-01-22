def Display():
    print("Jay Ganesh")

def chkGreater(a,b):
    if (a > b):
        print(f"{a} is greater than {b}")
    else:
        print(f"{b} is greater than {a}")

def square(a):
    return a**2

def cube(a):
    return a**3

def divisible(a):
    if (a%3==0 & a%5==0):
        print(f"{a} is divisible by 3 and 5")
    else:
        print(f"{a} is not divisible by 3 and 5")

def main():
    a = 0
    b = 0
    a = int(input("Enter 1st number: "))
    b = int(input("Enter 2nd number: "))

    Display()
    chkGreater(a,b)

    sq = square(a)
    print(f"square of number {a}:", sq)

    cu = cube(a)
    print(f"cube of number {a}:", cu)
    
    divisible(a)

if __name__ == "__main__":
    main()