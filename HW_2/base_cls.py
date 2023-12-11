import random


class Human:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    def human_method(self):
        return self.name, self.height, self.weight


class Woman(Human):
    def __init__(self, name, height, weight, surname, age):
        super().__init__(name, height, weight)
        self.surname = surname
        self.age = age

    def get_mail(self):
        return f'{self.name}_{self.surname}@mail.com'


choice_sport = ['Tennis', 'Football', 'Running', 'Boxing']


class Man(Woman):
    def greet_method(self):
        print(f'Hello, my name is {self.name}')

    def random_sport(self):
        print(f'Сегодня вечером {self.name} выбирает', random.choice(choice_sport))


class Fridge(Human):
    def __init__(self, name, height, weight, price, color):
        super().__init__(name, height, weight)
        self.price = price
        self.color = color
        self.items = []

    def add_items(self, items):
        self.items.append(items)
        print(f'{items} положили в холодильник')


nat = Woman('natasha', 170, 55, 'ivanova', 35)
john = Man('John', 180, 80, 'Petrov', 40)

john.greet_method()
print(nat.get_mail())
print(nat.human_method())
# print(john.random_sport())
john.random_sport()


fridge = Fridge("Холодильник", 200, 100, 500, "белый")
fridge.add_items("Молоко")
fridge.add_items("Яйца")
print(fridge.items)
