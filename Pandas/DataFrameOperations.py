import pandas as pd
import numpy as np

weather_df=pd.read_excel('6-weather.xlsx')
print(weather_df)
print("-----")
print(weather_df.head()) #ilk 5 satırı gösterir
print("--------")
print(weather_df.info())
print("----------")

print(weather_df.describe())
print("-----")
print(weather_df.count())
print(weather_df.isna()) #Eksik data var mı yok mu