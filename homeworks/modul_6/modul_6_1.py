class Vehicle:
     def __init__(self,owner,model,color,engine_power):
         self.owner = owner
         self.__model = model
         self.__engine_power = engine_power
         self.__color = color
         self.__COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
     def get_model(self):
        print(f"Модель: {self.__model}")
     def get_horsepower(self):
        print(f"Мощность двигателя: {self.__engine_power }")
     def get_color(self):
        print(f"Цвет: {self.__color}")
     def print_info(self):
        self.get_model()
        self.get_horsepower()
        self.get_color()
     def set_color(self,new_color):
        b=False
        for i in self.__COLOR_VARIANTS:
            if i == new_color.lower():
                b=True
        if b == False:
            print(f"Нельзя сменить цвет на {new_color}")

        else:
            self.__color =new_color


class Sedan (Vehicle):
    pass


# Текущие цвета __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'blue', 500)



# Изначальные свойства

vehicle1.print_info()



# Меняем свойства (в т.ч. вызывая методы)

vehicle1.set_color('Pink')

vehicle1.set_color('BLACK')

vehicle1.owner = 'Vasyok'



# Проверяем что поменялось

vehicle1.print_info()

