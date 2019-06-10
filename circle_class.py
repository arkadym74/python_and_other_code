"""
Circle Class

Write a Python class named `Circle` with the radius as an instance variable.

Your class should include two methods to calculate the area and the perimeter of a circle.
You can find the formula for both here: http://mathforum.org/dr.math/faq/formulas/faq.circle.html
Instantiate a Circle and call both methods.

You can use 3.14159 for the value of pi for simplicity. For extra credit, use the Math module to obtain pi.
"""
from math import pi
class Circle: 

    def __init__(self, radius):
       self.radius = radius

    def area(self):
        area = float(pi * self.radius * self.radius)
        print(f"Area of a circle is: {area:.2f}")
    
    def perimeter(self):
        circumference = float(2 * pi * self.radius)
        print(f"Perimeter of a circle is: {circumference:.2f}") 


area = Circle(4)
perimeter = Circle(5)

area.area()
perimeter.perimeter()



