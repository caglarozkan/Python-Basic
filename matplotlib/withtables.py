import matplotlib.pyplot as plt
import numpy as np

nump_arr1=np.random.randint(0,15,10) #0 ile 50 arası 10 tane tam sayı
nump_arr1.sort()

nump_arr2=np.random.randint(0,20,10)
nump_arr2.sort()

plt.subplot(1,2,1) #1 tane row olsun 2 tane column olsun ve su an 1. çiziliyor demek
plt.plot(nump_arr1,nump_arr2,"r")

plt.subplot(1,2,2)#bu da sonuncu indeksteki sayı yani 2. tabloyu çiziyorum demek
plt.plot(nump_arr2,nump_arr1,"b*-")
plt.savefig("Double plots.png")
plt.show()


my_figure = plt.figure()
figure_axes=my_figure.add_axes((0.1,0.1,0.7,0.7)) #0,7 ilk olan genişlik 2. 0.7 ise yükseklik yani %70 gibi düşünülebilir
figure_axes.plot(nump_arr1,nump_arr2,"g")
figure_axes.set_title("Graph Title")
figure_axes.set_xlabel("X-Axis")
figure_axes.set_ylabel("Y-Axis")
plt.show()

new_figure = plt.figure(dpi=100) # çözünürlük
new_figure_axes=new_figure.add_axes((0.1,0.1,0.7,0.7))
new_figure_axes.plot(nump_arr1,nump_arr1**2,"r*-")
new_figure_axes.plot(nump_arr1,nump_arr1**3,"g*-")
new_figure_axes.legend(["nump1**2","nump1**3"])
new_figure_axes.set_xlabel("X axis")
new_figure_axes.set_ylabel("Y axis")
new_figure_axes.set_label("")
plt.savefig("2 line 1 graph.png")
plt.show()