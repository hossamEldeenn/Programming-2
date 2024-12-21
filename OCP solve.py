class Shape:
    def __init__(self):
        pass

    def calculate_area(self):
        pass


class Rectangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width
        
    def calculate_area(self):
        return self.height * self.width
    
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
        
    def calculate_area(self):
        return (22/7) * self.radius**2

