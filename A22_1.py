class Demo:
    value = 5

    def __init__(self, A, B):
        self.No1 = A
        self.No2 = B

    def Fun(self):
        print("Inside instance method Fun: ", self.No1, self.No2)

    def Gun(self):
        print("Inside instance method Gun: ", self.No1, self.No2)

obj1 = Demo(11,21)
obj2 = Demo(51,101)

obj1.Fun()
obj1.Gun()
obj2.Fun()
obj2.Gun()