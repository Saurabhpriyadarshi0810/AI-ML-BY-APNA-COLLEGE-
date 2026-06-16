class Animal:
    def eat(self):
        print("Eating")

class Dog(Animal):
    pass

class Cat(Animal):
    def eat(self):
        print("cat is eating.")

d = Dog()
d.eat()
c = Cat()
c.eat()


# Single:-
# A -> B

# Multilevel:-
# A -> B -> C
class A:
    pass

class B(A):
    pass

class C(B):
    pass


#multiple :-
class A:
    pass

class B:
    pass

class C(A, B):
    pass

#herachial :-
# A and b both inherit same class 