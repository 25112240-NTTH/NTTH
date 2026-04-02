import math

class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

class Circle:
    def __init__(self, center, radius):
        self.center = Point(center.x, center.y)
        self.radius = radius

def point_in_circle(point, circle):
    distance = math.sqrt((point.x - circle.center.x)**2 + (point.y - circle.center.y)**2)
    return distance <= circle.radius