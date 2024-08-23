import random
from constants import *
import os


class SaveState:
    def __init__(self, username: str) -> None:
        self.username = username
        self.path = self.init_dir()

    def init_dir(self):
        """
        Создает директорию с файлом пользователя, если такого нет.
        """
        dirname = "users"
        path = f"{dirname}/{self.username}.txt"
        if not os.path.exists(dirname):
            os.mkdir(dirname)
        open(path, mode="a")
        return path

    def save_data(self, character):
        """
        Сохраняет в path значения атрибутов character
        """
        data = character.__dict__
        with open(self.path, "w") as file:
            for key, value in data.items():
                file.write(f"{key}:{value}\n")

    def read_data(self):
        """
        Считывает из path значения атрибутов
        """
        with open(self.path) as file:
            data = file.read().strip().split("\n")
        if len(data) < 4:
            return None
        attrs = dict()
        for attribute in data:
            name, number = attribute.split(":")
            attrs[name] = int(number)
        return attrs
    
    def be_dead(self):
        os.remove(self.path)


class Pet:
    def __init__(self):
        self.love = random.randint(0, 100)
        self.satiety = random.randint(0, 100)
        self.happiness = random.randint(0, 100)
        self.energy = random.randint(0, 100)

    def set_one_limit(self, stat: int):
        if stat > 100:
            stat = 100
        elif stat < 0:
            stat = 0
        return stat

    def set_limits(self):
        self.love = self.set_one_limit(self.love)
        self.satiety = self.set_one_limit(self.satiety)
        self.happiness = self.set_one_limit(self.happiness)
        self.energy = self.set_one_limit(self.energy)

    def decrease_stats(self, carousel: bool = False):
        vars = ["сытость", "энергия"]
        if carousel:
            vars += ["любовь", "счастье"]
        option = random.choice(vars)
        minus = random.randint(1, 5)
        if option == "сытость":
            self.satiety -= minus
        elif option == "энергия":
            self.energy -= minus
        elif option == "любовь":
            self.love -= minus
        else:
            self.happiness -= minus

    def increase_love(self):
        """гладить"""
        self.love += random.randint(5, 10)
        self.happiness += random.randint(1, 2)
        self.decrease_stats()
        self.set_limits()
        sticker = random.choice(LOVE_STICKERS)
        message = random.choice(LOVE_PHRASES)
        return sticker, message

    def increase_happiness(self):
        """играть"""
        self.happiness += random.randint(5, 10)
        self.satiety -= random.randint(5, 10)
        self.love += random.randint(1, 3)
        self.decrease_stats()
        self.set_limits()
        sticker = random.choice(PLAY_STICKERS)
        message = random.choice(PLAY_PHRASES)
        return sticker, message

    def increase_satiety(self):
        """кормить"""
        self.satiety += random.randint(10, 20)
        self.happiness += random.randint(1, 3)
        self.decrease_stats(True)
        self.set_limits()
        sticker = random.choice(FOOD_STICKERS)
        message = random.choice(FOOD_PHRASES)
        return sticker, message

    def increase_energy(self):
        """уложить спать"""
        self.energy += random.randint(1, 100)
        for i in range(random.randint(1, 4)):
            self.decrease_stats(True)
        self.set_limits()
        sticker = SLEEP_STICK
        message = "Тамагочи ушел спать, чтобы воcполнить энергию"
        return sticker, message

    def hello(self):
        sticker = random.choice(HELLO_STICKERS)
        message = random.choice(HELLO_PHRASES)
        return sticker, message


if __name__ == "__main__":
    pet = Pet()
    print(pet.__dict__)
    
    pet.__dict__ = SaveState("test").read_data()
    print(pet.__dict__)