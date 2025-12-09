import pandas as pd

df1 = pd.read_csv("7-concat_data1.csv")
print(df1)
df2 = pd.read_csv("7-concat_data2.csv")
print(df2)

#Concat
print("\n--- Concat ---")
df_concat=pd.concat([df1,df2],ignore_index=True) #ignore_index -> indexleri göz ardı et
print(df_concat)

#Merge
print("\n--- Merge ---")
df_merge1 = pd.read_csv("7-merge_data1.csv")
df_merge2 = pd.read_csv("7-merge_data2.csv")
print(df_merge1)
print(df_merge2)

print("\n---Merge outer-join ---")
df_merged_outer=pd.merge(df_merge1,df_merge2, on="Employee_ID",how="outer") # 2 tabloyu da birleştiriyor. Bilinmeyen yerleri NaN ile dolduruyor
print(df_merged_outer)

print("\n---Merge left-join ----")
df_merged_left=pd.merge(df_merge1,df_merge2,on="Employee_ID",how="left")
print(df_merged_left)# 1. tabloyu baz alıyor, eger 2. tabloda 1. tablodakilerle ilgili bilgiler varsa alıyor yoksa almıyor.

print("\n---Merge right-join ----")
df_merged_right=pd.merge(df_merge1,df_merge2,on="Employee_ID",how="right")
print(df_merged_right)

print("\n---Merge inner-join ----")
df_merged=pd.merge(df_merge1,df_merge2,on="Employee_ID",how="inner") #Kesişim olanları alıyor
print(df_merged)