import numpy as np
import pandas as pd
#---CSV----

df=pd.read_csv("6-employee.csv")
print(df)
print(df.describe()) #yapılabilen datalara yapıyo
print(df.count())

print("---Grouped---")
df_grouped =df.groupby("Department")
print(df_grouped.describe())
print(df_grouped.count())

print("---City Salary Mean---")
df_grouped_city=df.groupby("City")
print(df_grouped_city["Salary"].mean())
