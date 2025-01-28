class Animal :
    def __init__(self,name ,fed = False,alive = True):
        self.name =name
        self.fed =fed
        self.alive =alive
class Plant:
    def __init__(self, name ,edible = False):
        self.name =name
        self.edible = edible
# дочерние к животным
class Mammal(Animal):
    def eat(self, food):
        if food.edible == False:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False
        else:
            print(f"{self.name} съел {food.name}")
            self.fed = True

class Predator(Animal):
    def eat(self, food):
        if food.edible == False:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False
        else:
            print(f"{self.name} съел {food.name}")
            self.fed = True


#дочерние к растениям
class Flower(Plant):
    def __init__(self,name):
        self.name = name
        self.edible = False
class Fruit (Plant):
    def __init__(self, name):
        self.name = name
        self.edible = True

a1 = Predator('Волк с Уолл-Стрит')

a2 = Mammal('Хатико')

p1 = Flower('Цветик семицветик')

p2 = Fruit('Заводной апельсин')



print(a1.name)

print(p1.name)



print(a1.alive)

print(a2.fed)

a1.eat(p1)

a2.eat(p2)

print(a1.alive)

print(a2.fed)

