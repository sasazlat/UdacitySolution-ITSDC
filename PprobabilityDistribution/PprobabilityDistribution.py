import math

radius = 10.0
diameter = 2 * radius
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2

print("Radius is", radius)
print("Diameter is", diameter)
print("Circumference is", circumference)
print("Area is", area)

sqr_root_2 = math.sqrt(2)

is_sqr_root_2_an_integer = isinstance(sqr_root_2, int)
print("Is square root two an integer?", is_sqr_root_2_an_integer)

is_sqr_root_2_a_float = isinstance(sqr_root_2, float)
print("Is square root two a float?", is_sqr_root_2_a_float)
