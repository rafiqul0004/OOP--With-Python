from math import pi
class Shape:
    def __init__(self,name) -> None:
        self.name=name
class Rectangular(Shape):
    def __init__(self, name,height,width) -> None:
        self.height=height
        self.width=width
        super().__init__(name)
    def area(self):
        print( self.height*self.width)
class Circle(Shape):
    def __init__(self, name,radius) -> None:
        self.radius=radius
        super().__init__(name)
    def area(self):
        print( pi*self.radius*self.radius)
class Triangle(Shape):
    def __init__(self, name,height,base) -> None:
        self.height=height
        self.base=base
        super().__init__(name)
    def area(self):
        print(.5*self.base*self.height)
class Square(Shape):
    def __init__(self, name,side) -> None:
        self.side=side
        super().__init__(name)
    def area(self):
        print( 4*self.side*self.side)
rectangular=Rectangular('rectangular',2,3)
circle=Circle('circle',2)
triangle=Triangle('triangle',2,3)
square=Square('square',2)
shapes=[rectangular,circle,triangle,square]
for shape in shapes:
    print(shape.name)
    shape.area()