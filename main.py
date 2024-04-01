class Warrior():

    def __init__(self, name, power, endurance, hair_color): # Создаем свойства/характеристики объекта класса Warrior
        self.name = name # имя
        self.power = power # сила
        self.endurance = endurance # выносливость
        self.hair_color = hair_color # цвет волос

    # А теперь создаём методы того, что может делать объект класса Warrior

    def sleep(self): # Метод Спать
        print(f"Воин {self.name} лёт спать")
        self.endurance += 2

    def eat(self): # Метод Кушать
        print(f"Воин {self.name} решил подкрепиться")
        self.power += 1

    def hit(self): # Метод Драться
        print(f"Воин {self.name} дерётся")
        self.endurance -= 6

    def walk(self): # Метод Ходить
        print(f"Воин {self.name} решил прогуляться")

    def info(self): # Метод Вывод всей инфы о воине
        print(f"Имя воина - {self.name}")
        print(f"Его сила - {self.power}")
        print(f"Его выносливость - {self.endurance}")
        print(f"А цвет его волос - {self.hair_color}")

# Создаём объект класса Warrior

warrior1 = Warrior("Добрыня Никитич", 76, 54, "светло-русый")
warrior2 = Warrior("Алёша Попович", 45, 23, "шатен")

# print(warrior1.name)
# print(warrior1.power)
# print(warrior1.endurance)
# print(warrior1.hair_color)


# print(warrior1.endurance)
# warrior1.sleep()
# print(warrior1.endurance)
# print(warrior1.power)
# warrior1.eat()
# print(warrior1.power)

warrior1.info()
warrior1.sleep()
warrior1.eat()
warrior1.hit()
warrior1.walk()

warrior2.info()
warrior2.sleep()
warrior2.eat()
warrior2.hit()
warrior2.walk()



