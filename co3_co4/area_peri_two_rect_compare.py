#Create Rectangle class with attributes length and breadth and methods to find area and perimeter.
# Compare two Rectangle objects by their area.

class rectangle():
    def __init__(self,l,w,):
        self.length=l
        self.width=w
    def rectangle_area(self):
        return self.length*self.width
    def rectangle_peri(self):
        return 2*(self.length*self.width)
l1= float(input("enter length of first rectangle: " ))
w1=float(input("Enter width of first rectangle: "))
l2= float(input("enter length of second rectangle: " ))
w2=float(input("Enter width of second rectangle: "))
ob1=rectangle(l1,w1)
ob2=rectangle(l2,w2)
print("Area of first rectangle is {} and perimeter of first rectangle is {}: ".format(ob1.rectangle_area(),ob1.rectangle_peri()))
print("Area of first rectangle is {} and perimeter of first rectangle is {}: ".format(ob2.rectangle_area(),ob2.rectangle_peri()))
print(ob1.rectangle_area()>ob2.rectangle_area())


