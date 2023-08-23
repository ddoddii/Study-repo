class Square:
    def __init__(self,side):
        self.side = side
    def area(self):
        return self.side * self.side
class SquarePrism(Square):
    def __init__(self,side,height):
        self.side = side
        self.height = height
    def area(self):
        base_area = super().area() #Square 의 area 함수를 상속받음
        lateral_area = self.side * self.height
        return 2 * base_area + 4 * lateral_area
class Cube(SquarePrism):
    def __init__(self,side):
        super().__init__(side=side,height=side)
    def area(self):
        return super().area() * 100

x = Cube(2)
print(x.area())