import numpy as np

my_matrix=[[5,10],[15,20]]
print(my_matrix)
#(row,column)
matrix=np.random.randn(3,2)#(3=row,2=column)
print(matrix)
print(matrix[1][0])

first_array=np.array([[10,20],[30,40]])
second_array=np.array([[4,9],[13,16]])

print(first_array +second_array)

third_array=np.array([[50,60]]) # bu da aslında 1,2lik bir matrix o yüzden 2,2lik olanla toplanabilir
print(first_array+third_array) #third_arrayin ilk satırı 50 60 olarak verilmiş fakat 2. satırı verilmmeiş burda toplarken 2. satırı da 50 60 gibi algılayıp toplama işlemi yapılıyor

fourth_array=np.array([[10,20,30,40,50]]) #1,5lik bir matrix
print(fourth_array.shape)
#!!!HATAAA print(first_array+fourth_array) #2,2 olan bir matrixle 1,5 olan toplanamaz