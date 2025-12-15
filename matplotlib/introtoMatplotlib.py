import numpy as np
import matplotlib.pyplot as plt

age_list=[10,15,20,25,40,50,67,87,88,90,99]

weight_list=[123,65,32,65,245,76,32,76,27,76,65]

plt.plot(age_list,weight_list,"g") # y->yellow r,g,b kullanabiliyoruz çizilecek çizginin rengi için
#pl.plot(x ekseni,y ekseni)
plt.xlabel("age") #x eksenini isimlendiriyoruz
plt.ylabel("weight")#y eksenini isimlendiriyoruz
plt.title("Age-Weight") #TABLONUN başlıgı
plt.savefig("first table.png") #kaydediyor.
plt.show() #plt show çalıştıktan sonra ekranı temizler o yüzden öncesinde kaydetmemiz gerekir

print("---------")
np_age_list=np.array(age_list)
np_weight_list=np.array(weight_list)

plt.plot(np_age_list,np_weight_list,"r")
plt.show()

nump_arr1=np.linspace(0,20,15) #linspace fonksiyonu 0dan 20ye kadar 15 tane sayı üretecek ve bunlar eşit aralıklı olacak
nump_arr2=nump_arr1**3
plt.plot(nump_arr1,nump_arr2,"b*-")#*data pointleri göstererek çizer
plt.xlabel("nums")
plt.ylabel("nums-cubes")
plt.savefig("exponential test.png")
plt.show()