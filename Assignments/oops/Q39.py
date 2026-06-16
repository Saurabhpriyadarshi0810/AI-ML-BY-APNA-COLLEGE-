class Herbivore:

    def eat_plants(self):
        print("Herbivore eats plants.")


class Carnivore:

    def eat_meat(self):
        print("Carnivore eats meat.")


class Omnivore:

    def eat_both(self):
        print("Omnivore eats both plants and meat.")


class Bear(Herbivore, Carnivore, Omnivore):

    def display(self):
        print("Bear is an omnivorous animal.")



b = Bear()

b.display()
b.eat_plants()
b.eat_meat()
b.eat_both()