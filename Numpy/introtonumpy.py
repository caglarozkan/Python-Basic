import numpy as np
#pip install numpy

my_list=[10,20,30]
print(type(my_list))

my_numpy_array=np.array(my_list)
print(type(my_numpy_array),"--",my_numpy_array)

list1=[10,20,30]
list2=[10,20,30]
print(list1 + list2)

np_list1=np.array(list1)
np_list2=np.array(list2)
print(np_list1 + np_list2)
#print(np_list1 - np_list2)
#print(np_list1 * np_list2)
#print(np_list1 // np_list2)

other_array=np.array([10,20,30,40,50])
print("min:",other_array.min(),"max:",other_array.max(),"sum:",other_array.sum())
#print(other_array + np_list1) !!HATA çünkü eşit boyutta degiller birisi 3 elemanlı digeri 5 elemanlı
