class Person:

    def __init__(self, name, age=None, address=None):
        self.name = name
        self.age = age
        self.address = address

    def display(self):
        print(f"{self.name}\n{self.age}\n{self.address}")


p1 = Person("Saurabh")
p2 = Person("Saurabh", 20)
p3 = Person("Saurabh", 20, "hajipur")

p1.display()
p2.display()
p3.display()