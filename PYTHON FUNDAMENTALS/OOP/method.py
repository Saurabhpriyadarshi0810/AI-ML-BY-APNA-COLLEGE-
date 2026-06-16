# instance metthod 
class Student:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(self.name)

# class method 
class Student:
    school = "ABC"

    @classmethod
    def get_school(cls):
        return cls.school
    
print(Student.get_school())

#static method 

class Math:

    @staticmethod
    def add(a, b):
        return a + b

print(Math.add(2, 3))