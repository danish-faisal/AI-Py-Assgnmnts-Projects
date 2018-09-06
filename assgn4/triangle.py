import math

class Triangle:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c

    def perimeter(self):
        x=self.a+self.b+self.c
        return x
    def area(self):
        s=(self.a+self.b+self.c)/2
        ar=math.sqrt(s*(s-self.a)*(s-self.b)*(s-self.c))
        return ar

x=int(input("Input the measure of 1st side of the triangle:"))
y=int(input("Input the measure of 2nd side of the triangle:"))
z=int(input("Input the measure of 3rd side of the triangle:"))
t=Triangle(x,y,z)
print("Area:",t.area(),"\nPerimeter:",t.perimeter())
