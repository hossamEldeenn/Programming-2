class Shape:
    def __init__(self, shape_type, **kwargs):
        self.shape_type = shape_type
        
        if self.shape_type == "Rectangle":
            self.height = kwargs['height']
            self.width = kwargs['width']
        
        elif self.shape_type == "Circle":
            self.radius = kwargs['radius']

    def calculate_area(self):
        
        if self.shape_type == "Rectangle":
            return self.height * self.width
        
        elif self.shape_type == "Circle":
            return (22/7) * self.radius**2
