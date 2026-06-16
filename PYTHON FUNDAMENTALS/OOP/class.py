class Student:
    school = "ABC School"

    def __init__(self, name):
        self.name = name

s1 = Student("Rahul")
s2 = Student("Amit")

print(s1.school)
print(s2.school)