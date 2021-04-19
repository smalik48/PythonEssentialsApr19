#importing math lib to get the value of pi
import math

#get the radius from the user, convert to float as radius can be anything
radius = float(input("Please Provide the Radius of the Circle: "))

#calculate the circumference with 2*pi*r
Circumference = 2 * math.pi * radius

print(Circumference)