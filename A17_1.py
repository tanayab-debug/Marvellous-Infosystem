import Arithmetic 


A = int(input("Enter 1st number: "))
B = int(input("Enter 2nd number:"))

ret = Arithmetic.Add(A,B)
print("Addition of numbers is: ", ret)

ret = Arithmetic.Sub(A,B)
print("Subtraction of numbers is: ", ret)

ret = Arithmetic.Mul(A,B)
print("Multiplition of numbers is: ", ret)

ret = Arithmetic.Div(A,B)
print("Division of numbers is: ", ret)