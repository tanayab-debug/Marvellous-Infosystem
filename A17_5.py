def prime(no):
    for i in range(2,no):
        if (no %i == 0):
            return False
        else:
            return True
        
def main():
    no = 0
    no = int(input("Enter the number: "))
    ret = prime(no)
    if(ret == False):
        print("not prime number") 
    else:
        print("prime number") 

if __name__ == "__main__":
    main()