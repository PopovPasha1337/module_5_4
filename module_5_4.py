class House:
    houses_history = []
    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return super().__new__(cls)
    def __init__(self, name, floors):
        self.name = name
        self.floors = floors
    def __del__(self):
        print(f'{self.name} снесен. но он станется в истории')


h1 = House('Жк Эльбрус', 10)
print(House.houses_history)
h2 = House('Жк Акация', 20)
print(House.houses_history)
h3 = House('Жк Матрешки', 20)
print(House.houses_history)

del h2
del h3
print(House.houses_history)