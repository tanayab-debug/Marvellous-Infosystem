def chk(char):
    vowels = ["a","e","i","o","u"]
    i = char.lower()
    if i in vowels:
        print("vowel") 
    else:
        print("consonant")

def factors(no):
    for i in range(1,no+1):
        if no % i == 0:
            print(i)

def operations():
    a = int(input("enter 1st number: "))
    b = int(input("enter 2nd number: "))

    print("addition is: ", a+b)
    print("subtion is: ", a-b)
    print("diviion is: ", a/b)
    print("multiplition is: ", a*b)

def ascending(a):
    print("ascending order: ")
    for i in range(1,a+1):
        print(i)

def descending(a):
    print("descending order: ")
    for i in range(a,0,-1):
        print(i)

def main():
    char =  input(print("enter the character: "))
    chk(char)

    a = 0
    a = int(input("enter a number: "))
    factors(a)

    operations()

    ascending(a)
    
    descending(a)

if __name__ == "__main__":
    main() 