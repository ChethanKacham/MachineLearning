# Question - 5

import math

print("Question - 5")
radius_of_circle = 30
# Area of circle
_area_of_circle_ = math.pi * radius_of_circle * radius_of_circle
print("Area of circle is", _area_of_circle_, "square metres")
# Circumference of circle
_circum_of_circle_ = 2 * math.pi * radius_of_circle
print("Circumference of circle is", _circum_of_circle_, "metres")
# Taking radius as user input and calculating area
radius_from_user = float(input("Please enter the radius of the circle: "))
_area_of_circle_from_user = math.pi * radius_from_user * radius_from_user
print("Area of circle by taking radius as input from user", _area_of_circle_from_user)