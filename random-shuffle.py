from random import randint
from random import shuffle

x=randint(0,100)#100 dahil
print(x)

my_list=[0,10,20,30,40,50,60,70]
print(my_list)

shuffle(my_list) #shuffle yapıyo listeye



print(my_list)
shuffle(my_list)
print(my_list)

print(my_list[randint(0,len(my_list)-1)])