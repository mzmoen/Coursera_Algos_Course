import math


class Circle:
    def __init__(self, radius=1):
        self._radius = radius

    def __repr__(self):
        return "Circle({0:g})".format(self.radius)

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, val):
        if val < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = val

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, val):
        self._radius = val / 2

    @property
    def area(self):
        return (self.radius ** 2) * math.pi

