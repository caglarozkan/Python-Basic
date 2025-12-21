import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv('athlete_events.csv')
print(data)
print(data.info())

sns.set_theme(style="darkgrid")

sns.scatterplot(x="Height",y="Weight",data=data, hue="Sex")#Hue vurgulanmak istenen column yazılır. Genelde kategorik degerler için kullanılır

plt.xlabel('Height of  Athletes')
plt.ylabel('Weight of  Athletes')
plt.title("Athletes Weight vs Height")
plt.savefig("Athletes Weight vs Height.png")
plt.show()

print(data["Medal"].unique()) #Medal degerlerini gösteriyor. Unique olarak


sns.set_style("whitegrid")
sns.lineplot(x="Height",y="Weight",data=data,hue="Sex")
plt.xlabel('Height of  Athletes')
plt.ylabel('Weight of  Athletes')
plt.title("Athletes Weight vs Height")
plt.savefig("Athletes Weight vs Height Line.png")
plt.show()

sns.set_style("darkgrid")
sns.displot(x="Height",data=data,hue="Sex") #kind="kde" Yazarsak histogram yerine çizgi gibi gösteriyor
plt.ylabel("Frequency")
plt.title("Athletes Height Distribution")
plt.savefig("Athletes Height Distribution.png")
plt.show()

sns.set_style("darkgrid")
sns.displot(x="Height",data=data,hue="Sex",kind="kde") #kind="kde" Yazarsak histogram yerine çizgi gibi gösteriyor
plt.ylabel("Frequency")
plt.title("Athletes Height Distribution")
plt.savefig("Athletes Height Distribution Line.png")
plt.show()

sns.barplot(x="Medal",y="Height",hue="Sex",data=data)
plt.title("Medals by Height")
plt.savefig("Medals by Height.png")
plt.show()