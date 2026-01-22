def prime(no):
    if (no<1):
        return False
    for i in range(2, (no**0.5) + 1):
        if no%i==0:
            return False
    return True

def chkLen(no):
    return len(str(no))

def sum(no):
    sum=0
    for num in str(no):
        digit = int(num)
        sum = sum + digit
    print(sum)

def reverse(no):
    num = str(no)[::-1]
    print(int(num))
    print("".join(reversed(str(no))))

def palindrome(no):
    return str(no) == str(no)[::-1]

def main():
    a = 0
    a = int(input("Enter 1st number: "))

    val = 0
    val = chkLen(a)
    print(val)
    
    reverse(a)

    if palindrome(a):
        print("Palindrome")
    else:
        print("NOt a palindrome")

    sum(a)

if __name__ == "__main__":
    main()