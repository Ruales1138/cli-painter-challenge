# TODO: Add code here
import matplotlib.pyplot as plt
from math import pi
class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
class Circle:
    def __init__(self, center: Point, radius: float):
        self.center = center
        self.radius = radius

    def area(self) -> float:
        return pi * (self.radius ** 2)

    def draw(self):
        circle = plt.Circle((self.center.x, self.center.y), self.radius, color="r")
        plt.gca().add_patch(circle)
        plt.axis("scaled")
        plt.show()
