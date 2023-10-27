import random
import math

class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self):
        # Generate random polar coordinates
        r = self.radius * math.sqrt(random.random())
        theta = 2 * math.pi * random.random()

        # Convert polar coordinates to Cartesian coordinates
        x = self.x_center + r * math.cos(theta)
        y = self.y_center + r * math.sin(theta)

        return [x, y]
