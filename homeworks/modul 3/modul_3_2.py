#1.Функция с параметрами по умолчанию:
def  print_params(a = 1, b = 'строка', c = True) :
    print( a,b,c)
print_params()
print_params(1, 5,0)
print_params("привет",0)
print_params("пока")
print_params(b = 25)
print_params(c = [1,2,3])
#2.Распаковка параметров:
values_list=(1,89,19)
values_dict={"это первый эл":1,False:'строка',15:True}
print_params(*values_list)
print_params(*values_dict)
#3.Распаковка + отдельные параметры:
values_list_2 = [True, 'Непонял!А понял!' ]
print_params(*values_list_2, 42)