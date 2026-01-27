import threading
import math

def Small(Str):
    cnt = 0
    for i in Str:
        if i.islower():
            cnt += 1
    print("The count of lowercase letters is: ", cnt)

def Capital(Str):
    cnt = 0
    for i in Str:
        if i.isupper():
            cnt += 1
    print("The count of uppercase letters is: ", cnt)

def Digit(Str):
    cnt = 0
    for i in Str:
        if i.isdigit():
            cnt += 1
    print("The count of digits is: ", cnt)

def main():
    print("Inside Thread: ", threading.get_ident())
    print("Inside Thread: ", threading.current_thread())
    Str = input("Enter String: ")

    t1= threading.Thread(target=Small, args=(Str,))
    t2= threading.Thread(target=Capital, args=(Str,))
    t3= threading.Thread(target=Digit, args=(Str,))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

if __name__ == "__main__":
    main()