import numpy as np
import pandas as pd

weather_na_df = pd.read_excel('6-weatherna.xlsx')
print(weather_na_df) #içerikte NaN olanlar var
print("----NaN Table---")
print(weather_na_df.isna())
print("Paris hakkında girilen bilgilerin sayısı:",weather_na_df["Paris"].count())

print("--dropna--")
print(weather_na_df.dropna()) #dropna fonksiyonu NaN buluna tüm rowları kaldırıyor
#print(weather_na_df.dropna(axis=1)) bu şekilde de içinde NaN olan tüm columnları siliyor
#inplace=True yaparsak degişiklik kalıcı olur

print(weather_na_df.fillna(20)) #NaN olan degerlerli 20 olarak degiştir

print("Mean of each city:",weather_na_df.mean())
weather_na_df.fillna(weather_na_df.mean(), inplace=True) #ortalama deger ile dolduruyo boş olanları
print(weather_na_df)