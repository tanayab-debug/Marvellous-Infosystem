class Arithmetic():

    def __init__(self):
        self.value1 = 0
        self.value2 = 0

    def Accept(self):
        self.value1 = int(input("Enter 1st number: "))
        self.value2 = int(input("Enter 2nd number: ")) 

    def Addition(self):
        return self.value1 + self.value2
    
    def Subtraction(self):
        return self.value1 - self.value2
    
    def Multiplication(self):
        return self.value1 * self.value2
    
    def Division(self):
        return self.value1/self.value2
    
obj = Arithmetic()
obj.Accept()
add = obj.Addition()
print("Addition of 2 digits is: ", add)
sub = obj.Subtraction()
print("Subtraction of 2 digits is: ", sub)
mul = obj.Multiplication()
print("Multiplication of 2 digits is: ", mul)
div = obj.Division()
print("Division of 2 digits is: ", div)

obj1 = Arithmetic()
obj1.Accept()
add1 = obj1.Addition()
print("Addition of 2 digits is: ", add1)
sub1 = obj1.Subtraction()
print("Subtraction of 2 digits is: ", sub1)
mul1 = obj1.Multiplication()
print("Multiplication of 2 digits is: ", mul1)
div1 = obj1.Division()
print("Division of 2 digits is: ", div1)