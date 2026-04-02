import copy

class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

class LineSegment:
    def __init__(self, d1 = None, d2 = None):
        if d1 is None and d2 is None:
            self._d1 = Point(8,5)
            self._d2 = Point(1,0)
        else:
            self._d1 = copy.deepcopy(d1)
            self._d2 = copy.deepcopy(d2)

@classmethod
def from_coordinates(cls, x1, y1, x2, y2):
    d1 = Point(x1, y1)
    d2 = Point(x2, y2)  
    return cls(d1, d2)

LineSegment(LineSegment S)
@classmethod
def from_copy(cls, other_segment):
    new_d1 = Point(other_segment._d1.x, other_segment._d1.y)
    new_d2 = Point(other_segment._d2.x, other_segment._d2.y)
    return cls(new_d1, new_d2)

def display(self):
    print(f"Điểm 1: ({self._d1.x}, {self._d1.y})")
    print(f"Điểm 2: ({self._d2.x}, {self._d2.y})")