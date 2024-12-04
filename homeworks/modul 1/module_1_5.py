immutable_var=1,2,3,4,5,True,False,"Git"
print(immutable_var)
# immutable_var[1]='logarifm'   # не сработает так как кортеж это неизменяемая структура
mutable_list=[1,2,3,4,5,True,False,"Git"]
print(mutable_list)
mutable_list[0]=4
mutable_list[7]='ДЗ готово'
print(mutable_list)