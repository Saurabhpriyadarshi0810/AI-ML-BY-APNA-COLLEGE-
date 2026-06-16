class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

Dog().sound()


#calling parent method

class Animal:
    def __init__(self):
        print("Animal")

class Dog(Animal):
    def __init__(self):
        super().__init__()
        print("Dog")

d = Dog()
