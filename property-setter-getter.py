class Shape:
    def __init__(self,a,b=-1):
        self.b=b
        self.a=a

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self,value):
        if not isinstance(value,int):
            raise TypeError("a must be an integer")
        else:
            self._a=value

    def area(self):
        return self.a*self.b

    @property
    def perimeter(self):
        return (self._a+self.b)*2

class Circle(Shape):
    def __init__(self,r):
        self.r=r

    def area(self):
        return 3.14*(self.r**2)

    @property
    def perimeter(self):
        return 2*3.14*self.r

class Square(Shape):
    def __init__(self,r):
        super().__init__(r,r)


newShape=Shape(10,20)
print("New Shape Area:",newShape.area())
print("New Shape Perimeter:",newShape.perimeter) #proprty(no())

newCircle=Circle(5)
print("Circle Area:",newCircle.area())
print("Circle Perimeter:",newCircle.perimeter)

newSquare=Square(7)
print("Square Area:",newSquare.area())
print("Square Perimeter:",newSquare.perimeter)
