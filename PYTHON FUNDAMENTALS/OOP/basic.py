class Student:
    pass

s1 = Student()
s2 = Student()

print(type(s1))


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Rahul", 20)

print(s1.name)
print(s1.age)

class Student:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print("My name is", self.name)

s1 = Student("Rahul")
s1.introduce()
