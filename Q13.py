import math
def area():
    len = int(input("enter length: "))
    wid = int(input("enter width: "))
    print("area of rectangle is: ", len*wid)

def ci_area():
    r = int(input("enter radius of the circel: "))
    print("area of circle: ", math.pi*r*r)

def mark():
    marks = int(input("enter marks: "))
    if (marks>=75):
        print("Distinction")
    elif (marks>=60):
        print("first class")
    elif (marks>=50):
        print("second class")
    else:
        print("Fail")

def per(no):
    sum = 0
    for i in range(1,no):
        if no%i==0:
            sum = sum + i

    if sum == no:
        print("perfect")
    else:
        print("imperfect")

def binary(no):
    binary = bin(no)
    print(binary)

def main():
    area()
    ci_area()
    mark()

    no = int(input("enter the number: "))
    per(no)
    binary(no)

if __name__ == "__main__":
    main()