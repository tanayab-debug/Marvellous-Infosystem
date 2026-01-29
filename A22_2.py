class Circle:
    PI = 3.14

    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self):
        self.Radius = int(input("Enter radius of circle: "))

    def CalculateArea(self):
        self.Area = self.PI * (self.Radius**2)

    def CalculateCircumference(self):
        self.Circumference = 2 *self.PI*self.Radius

    def Display(self):
        print("Radius of circle is: ", self.Radius)
        print("Area of circle is: ", self.Area)
        print("Circumference of circle is: ", self.Circumference) 

obj = Circle()
obj.Accept()
obj.CalculateArea()
obj.CalculateCircumference()
obj.Display()

obj1 = Circle()
obj1.Accept()
obj1.CalculateArea()
obj1.CalculateCircumference()
obj1.Display()