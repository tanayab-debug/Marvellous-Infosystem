class Numbers:

    def __init__(self):
        self.value = int(input("Enter the number: "))

    def ChkPrime(self):
        if(self.value <= 1):
            return False
        
        for i in range(2, self.value):
            if (self.value%i == 0):
                return False
            else:
                return True
            
    def Factors(self):
        print("Factors are: ")
        for i in range(1, self.value + 1):
            if(self.value%i == 0):
                print(i)

    def SumFactors(self):
        self.sum = 0
        for i in range(1, self.value + 1):
            if(self.value%i == 0):
                self.sum += i
        print("Sum of factors is ", self.sum)

    def perfect(self):
        self.v = 1
        for i in range(2, self.value):
            if (self.value%i == 0):
                self.v += i
        return self.v

obj = Numbers()
obj.Factors()
obj.SumFactors()
val = obj.ChkPrime()
if(val == True):
    print("It's a prime number")
else:
    print("It's not a prime number")

v1 = obj.perfect()
if(v1 == obj.value):
    print("It's a perfect number")
else:
    print("It's not a perfect number")