#method overridding

class Bird:
    def fly(self):
        pass

class Sparrow(Bird):
    def fly(self):
        print("Flying")

#duck typing 

class Dog:
    def speak(self):
        print("Bark")

class Cat:
    def speak(self):
        print("Meow")

def make_sound(animal):
    animal.speak()

#operator overloadig 

# same operator behave differently 
print(5 + 3)
print("A" + "B")