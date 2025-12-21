import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#boxplot
#median, quartile(%25, %50, %75), min max 1.5 * IQR, outllier

data=np.array([1,13,17,23,27,46,51,65,68,71,76,84,87,94,100])

plt.figure(figsize=(6,5))

sns.boxplot(y=data)
plt.title("Box Plot")
plt.ylabel("Data Value")
plt.grid(True)
plt.show()