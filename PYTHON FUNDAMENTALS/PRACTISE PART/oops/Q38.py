class Player:

    player_count = 0   

    def __init__(self, name, level):
        self.name = name
        self.level = level
        Player.player_count += 1

    def display(self):
        print(f"Player Name : {self.name}")
        print(f"Player Level : {self.level}")


# Creating Objects
p1 = Player("Saurabh", 10)
p2 = Player("Vaishnavi", 15)
p3 = Player("Rahul", 20)

p1.display()
print()

p2.display()
print()

p3.display()
print()

print(f"Total Players Created = {Player.player_count}")