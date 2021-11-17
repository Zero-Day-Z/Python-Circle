#Zakiya Talley - ITEC 345 - Circle Assignment Python
#Import Packages: Math to calculate circle, turtle to draw circle, time to add sleep function
import math
import turtle
import time
#create circle class
class Circle:
    pi=3.14159

    def __init__(self, radius):
        self.radius= radius

    def area (self):
        return (Circle.pi * math.pow(self.radius, 2))

#Calculate and print Area of Circle
r= int(input("Enter the radius of the circle"))
print("The radius is" , r)
c= Circle(r)
print("The area of the circle is: ", c.area())

#Draw Circle
window = turtle.Screen()
turtle.bgcolor("black")
turtle.color("red" , "red")
turtle.begin_fill()
turtle.circle(r)
turtle.end_fill()
#Note: Window does not respond while it is sleeping
time.sleep(10) #Sleep for 10 seconds to view circle
