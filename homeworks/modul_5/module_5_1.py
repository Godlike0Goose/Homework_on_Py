class House:
    def __init__(self,name,number):
        self.name=name
        self.number_of_floors=number
    def go_to(self,new_floor):
        if new_floor>self.number_of_floors or new_floor < 1:
            print("Такого этажа нет")
        else:
            for i in range(1,new_floor):
                print(i)

h1 = House('ЖК Горский', 18)

h2 = House('Домик в деревне', 2)

h1.go_to(5)

h2.go_to(10)