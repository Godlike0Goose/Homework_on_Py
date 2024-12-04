
my_dict={"a":1,"b":2,"c":3}
print(my_dict)
print(my_dict.get("a"))
print(my_dict.get("d","такого ключа нет"))
my_dict.update({"d":4,"e":5})
del my_dict["a"]
print('1')
print(my_dict)
my_set={1,2,3,4,5,7,5,6}
print(my_set)
my_set.add(10)
my_set.discard(4)
print(my_set)