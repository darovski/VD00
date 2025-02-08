from abc import ABC, abstractmethod

# Шаг 1: Создайте абстрактный класс для оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

# Шаг 2: Реализуйте конкретные типы оружия
class Sword(Weapon):
    def attack(self):
        return "Боец наносит удар мечом."

class Bow(Weapon):
    def attack(self):
        return "Боец наносит удар из лука."

# Шаг 3: Модифицируйте класс Fighter
class Fighter:
    def __init__(self, weapon: Weapon):
        self.weapon = weapon

    def change_weapon(self, weapon: Weapon):
        self.weapon = weapon

    def attack(self):
        return self.weapon.attack()

# Класс Monster
class Monster:
    def __init__(self):
        self.alive = True

    def defeat(self):
        self.alive = False
        return "Монстр побежден!"

# Шаг 4: Реализация боя
def battle(fighter: Fighter, monster: Monster):
    print(fighter.attack())
    print(monster.defeat())

# Демонстрация
def main():
    # Создаем бойца с мечом
    sword = Sword()
    fighter = Fighter(sword)
    monster = Monster()

    print("Боец выбирает меч.")
    battle(fighter, monster)

    # Изменяем оружие на лук
    print("\nБоец выбирает лук.")
    bow = Bow()
    fighter.change_weapon(bow)
    monster = Monster()  # Новый монстр для нового боя
    battle(fighter, monster)

if __name__ == "__main__":
    main()