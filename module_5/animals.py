# Наследование и полиморфизм

# Родительский класс, в котором определяется имя, здоровье
# и общий абстрактный рык (звук) для всех животных
class Animals:

    def __init__(self, name):
        self.name = name
        self.health = 100

        # Приватный атрибут "животное"
        self._who_am_i = "Животное"

        # Двойной приватный атрибут "Здоровье животного"
        self.__animal_health = 'Мое здоровье - ' + str(self.health) + ' процентов'


    def make_noize(self):
        print("Grrrrrrrrrrr")


# Далее идут подклассы котов и собак
class Cat(Animals):

    def make_noize(self):
        print("Meow")


class Dog(Animals):

    def make_noize(self):
        print("Gav-Gav")


cat1 = Cat("Barsik")
dog1 = Dog('Sharik')

dog1.make_noize()
cat1.make_noize()

print(dog1.name)

print(cat1._who_am_i)
print(cat1._Animals__animal_health)
