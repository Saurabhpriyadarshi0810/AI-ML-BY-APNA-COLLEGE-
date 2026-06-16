class shape :
    def area(self):
        pass

class triangle(shape):
    def area(self):
        print(f"area of triangle  is (0.5* base* height)  sq unit")

class rectangle(shape):
    def area(self):
        print(f"area of rectangle is (length * breadth) sq unit")

class circle(shape):
    def area(self):
        print(f"area of circle  (pi*radius*radius) sq unit")

c=circle()
c.area()

t = triangle()
t.area()

r = rectangle()
r.area()