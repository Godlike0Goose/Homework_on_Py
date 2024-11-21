import random
result=""
rand= random.randint(3,20)


for i in range(1,int(rand/2+1)):
    for j in range(1,rand):

        if rand%(j+i) == 0 and j!=i:
            result+=str(i)+str(j)





print ("Число:",rand)
print ("Подходящий пароль:",result)