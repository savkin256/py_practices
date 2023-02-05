import random

class Warrior:

    def __init__(self):
        self.health = 100

    def under_attack(self):
        self.health += -20


warrior1, warrior2 = Warrior(), Warrior()

while warrior1.health > 0 and warrior2.health > 0:
    if random.randint(0, 1) == 0:
        warrior1.under_attack()
        print("WARRIOR-2 attacks, WARRIOR-1's health is", warrior1.health)
    else:
        warrior2.under_attack()
        print("WARRIOR-1 attacks, WARRIOR-2's health is", warrior2.health)

if warrior1.health == 0:
    print("WARRIOR-2 WIN!!!")
else:
    print("WARRIOR-1 WIN!!!")