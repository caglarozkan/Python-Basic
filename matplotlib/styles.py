import numpy as np
import matplotlib.pyplot as plt

data1=np.linspace(0,8,9)
data2=data1**2

my_fig,my_axes=plt.subplots()
print(type(my_fig))
my_axes.plot(data1,data2,"r*-")
my_axes.plot(data2,data1,"b*-")
my_axes.legend(["data1-data2","data2-data1"])
plt.show()

#plot fonk içinde color="RGB kodu" yazarak istedigimiz renkten oluşturabiliriz
#plot fonk içinde alpha=0.5 yazarak da transparency oluşsturabailiriz

(new_fig,new_axes) = plt.subplots()

new_axes.plot(data1,data2+20,color="blue",linewidth=3.5)
new_axes.plot(data1,data2+30,color="red",linewidth=1.0)

new_axes.plot(data1,data2+40,color="green",linestyle="-.")
new_axes.plot(data1,data2+50,color="purple",linewidth=2.0, marker="o",markerfacecolor="yellow")
#linewidth -> kalınlıgı belirliyor
#marker -> data pointlere işaret bırakıyor.
#markerfacecolor -> o noktaların rengini belirliyor
plt.show()


#scatter
plt.scatter(data1,data2) #nokta nokta gösterir
plt.show()

new_Arr=np.random.randint(0,1000,50)
plt.hist(new_Arr)
plt.show()