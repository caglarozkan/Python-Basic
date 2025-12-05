import numpy as np

#Indexing & arranging

print(list(range(0,10)))

new_np_array = np.arange(0,20,2)
#print(new_np_array)
#print(new_np_array[3])
#print(new_np_array[3:5])
print(new_np_array[2:9:2]) #slicing

print("--random--")
#print(np.random.randn(3))  #3,1 boyutunda rastgele sayılar
random_np_array=np.random.randn(3,3) #3,3 boyutunda rastgele numaral içecen bir matrix veriyo
print(random_np_array)