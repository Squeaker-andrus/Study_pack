import time


class Auto:

    def __init__(self, brand: str, age: int, color: str, mark: str = "Noname", weight: int = 1500):
        self.brand = brand
        self.age = age
        self.color = color
        self.mark = mark
        self.weight = weight

    def move(self):
        return print("move")

    def birthday(self):
        self.age += 1
        return print(f"Возраст авто теперь равна {self.age} лет")

    def stop(self):
        return print("stop")

class Truck(Auto):

    def __init__(self, brand: str, age: int, color: str, max_load: int):
        super().__init__(brand, age, color, mark="Noname truck", weight=5500)
        self.max_load = max_load

    def move(self):
        print("attention")
        time.sleep(1)    # отсебятина пошла
        return super().move()

    def load(self):
        time.sleep(1)
        print("load") # данную функцию можно и поприкольнее сделать, типа задать обьем груза и чтобы он не превышал max_load, но лень
        time.sleep(1) # а так он просто будет вечно грузится


class Car(Auto):
    def __init__(self, brand: str, age: int, color: str, max_speed: int):
        super().__init__(brand, age, color, mark="Noname car")
        self.max_speed = max_speed

    def move(self):
        super().move()
        return print(f"max speed is {self.max_speed}")


tom_car = Car("BMV", 1, "blue", 200)
tom_car.mark = "X5"   # почему бы и нет

kevin_car = Car("Audi", 3, "gray", 180)
kevin_car.weight = 2000

frank_truck = Truck("MAN", 2, "darkgray", 7000)

rick_truck = Truck("Volvo", 4, "white", 20000)


print("Махинации с машиной Тома")
print(tom_car.brand)
print(tom_car.age)
print(tom_car.weight)
print(tom_car.mark)
print(tom_car.color)
tom_car.birthday()
tom_car.birthday()
tom_car.birthday()
print(tom_car.age)
print("Махинации с машиной Кевина")
print(kevin_car.weight)
print("Махинации с грузовиком Фрэнка")
frank_truck.move()
frank_truck.load()
frank_truck.load()
print("Махинации с грузовиком Рика")
rick_truck.move()
rick_truck.load()
rick_truck.load()
