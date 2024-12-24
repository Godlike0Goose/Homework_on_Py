class House:
    def __init__(self,name,number):
        self.name=name
        self.number_of_floors=number
    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"
    def __eq__(self, other):
        return self.number_of_floors == other.numper_of_floors
    # __lt__(<), __le__(<=), __gt__(>), __ge__(>=), __ne__(!=)
    def __lt__(self, other):
        return self.number_of_floors < other.numper_of_floors
    def __le__(self, other):
        return self.number_of_floors <= other.numper_of_floors
    def __gt__(self, other):
        return self.number_of_floors > other.numper_of_floors
    def __ge__(self, other):
        return self.number_of_floors >= other.numper_of_floors
    def __ne__(self, other):
        return self.number_of_floors != other.numper_of_floors
    def __add__(self, value) :
        self.number_of_floors+=value
        return self
    def __iadd__ (self, value) :
        self.number_of_floors += value
        return self
    def __radd__(self,value):
        self.number_of_floors += value
        return self
    def go_to(self,new_floor):
        if new_floor>self.number_of_floors or new_floor < 1:

            print("Такого этажа нет")
        else:
            for i in range(1,new_floor):
                print(i)