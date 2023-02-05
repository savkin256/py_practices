import random


class Warrior:

    def __init__(self):
        self.health = 100
        self.armor = 100
        self.endurance = 100
        self.is_attacking = False

    def defence(self, opponent_attacks, opponent_endurance):
        if opponent_attacks:
            if self.armor > 0 and opponent_endurance > 0:
                self.health -= random.randint(0, 20)
                self.armor -= random.randint(0, 10)
            elif self.armor > 0 and opponent_endurance <= 0:
                self.health -= random.randint(0, 10)
                self.armor -= random.randint(0, 10)
            elif self.armor <= 0 and opponent_endurance > 0:
                self.health -= random.randint(10, 30)
            else:
                self.health -= random.randint(0, 10)

    def attack(self, opponent_attacks, opponent_endurance):
        if opponent_attacks and opponent_endurance > 0:
            self.health -= random.randint(10, 30)
            self.endurance -= 10
        elif opponent_attacks and opponent_endurance <= 0:
            self.health -= random.randint(0, 10)
            self.endurance -= 10
        else:
            self.endurance -= 10


def main():
    warrior1, warrior2 = Warrior(), Warrior()
    
    while warrior1.health > 10 and warrior2.health > 10:
        warrior1.is_attacking, warrior2.is_attacking = random.choice([True, False]), random.choice([True, False])
    
        if warrior1.is_attacking:
            warrior1.attack(warrior2.is_attacking, warrior2.endurance)
            print("WARRIOR-1 is attacking, ", end="")
        else:
            warrior1.defence(warrior2.is_attacking, warrior2.endurance)
            print("WARRIOR-1 is defencing, ", end="")
    
        if warrior2.is_attacking:
            warrior2.attack(warrior1.is_attacking, warrior1.endurance)
            print("WARRIOR-2 is attacking. ")
        else:
            warrior2.defence(warrior1.is_attacking, warrior1.endurance)
            print("WARRIOR-2 is defencing. ")
    
        print("WARRIOR-1: health = ", warrior1.health, ", armor = ", warrior1.armor, ", endurance = ", warrior1.endurance)
        print("WARRIOR-2: health = ", warrior2.health, ", armor = ", warrior2.armor, ", endurance = ", warrior2.endurance, "\n")
    
    if warrior1.health <= 10 and warrior2.health > 10:
        print("WARRIOR-2 WIN!!!")
        print("Should he kill WARRIOR-1?")
    elif warrior2.health <= 10 and warrior1.health > 10:
        print("WARRIOR-1 WIN!!!")
        print("Should he kill WARRIOR-2?")
    elif warrior1.health < warrior2.health:
        print("WARRIOR-2 WIN!!!")
        print("Should he kill WARRIOR-1?")
    else:
        print("WARRIOR-1 WIN!!!")
        print("Should he kill WARRIOR-2?")
    
    flag = True
    
    while flag:
        answer = input()
        if answer.lower() == "yes":
            print("DONE!  REST IN PEACE, brave warrior ...")
            flag = False
        elif answer.lower() == "no":
            print("I SAVED YOUR LIFE")
            flag = False
        else:
            print("Please, just YES or NO")


if __name__ == '__main__':
    main()