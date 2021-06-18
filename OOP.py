class Dragon:
    def __init__(self, name, damage):
        self.__nature = " Дракон"
        self._family = "Обычный"
        self.name = name
        self.damage = damage

    def attack(self):
        attacking_name = self.name
        attacking_damage = self.damage
        print(
            self._family,
            self.__nature,
            attacking_name,
            " бьет и наносит ",
            attacking_damage,
            " урона",
        )

    def ulta(self):
        print(self.name, "ЖЖОТ ~~~~~~~~×< и наносит ", self.damage, " урона")


class IceDragon(Dragon):
    # def __init__(self, name, damage, _family="Ледяной"):

    def __init__(self, name, damage):
        super().__init__(name, damage)
        self._family = "Ледяной"

    def ulta(self):
        self.damage = self.damage * 2
        print(self.name, "ОХЛАЖДАЕТ =======( и наносит ", self.damage, " урона")


dragon1 = Dragon("Глаурунг", 100)
dragon2 = IceDragon("Хладнокрыл", 75)
dragon1.attack()
dragon2.attack()
dragon1.ulta()
dragon2.ulta()
print(dragon1.__dir__())
print(dragon2.__dir__())
del dragon2.name
print(dragon2.__dir__())
print(dragon2.name)