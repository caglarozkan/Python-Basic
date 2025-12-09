import pandas as pd
import numpy as np

#DataFrame

data=np.random.randn(4,3) #4,3 boyutunda rastgele sayılar
# !!!!data_frame=pd.Series(data) Series tek boyutlu datalarda çalışır
data_frame=pd.DataFrame(data)
print(data_frame,type(data_frame))
print("-------")

new_df=pd.DataFrame(data, index=["Caglar","Ahmet","Emre","Yigit"], columns=["Salary","Age","Seniority"]) #4x3
print(new_df)
print(new_df[["Salary","Age"]])
print("------")
print(new_df.loc["Caglar"]) #.loc() ile o row'a ulaşabiliyoruz
print("---")
print(new_df.iloc[2])  #2.indexteki rowu print eder
print(new_df.iloc[:,2])  #  : bütün rowları seçer , kullanarak istedigimiz columnu seçeriz

print("Salary of Emre:",new_df.loc["Emre"]["Salary"])
print("-----------")
#Data Manipulation

new_df["Extra"]=10 #bu şekilde yeni bir column oluşturabiliyoruz. Bütün degerleri 10 yapacak
print(new_df)
new_df.drop("Extra", axis=1,inplace=True) #1->column 0-> row siliyor. inplace->True yaparsak içeride degişim yapıyor ama False olursa yeni bir frame oluşlturuyor ve atama yaparak kullanabiliriz yeni oluşanı
print(new_df)
print(new_df>0)
print(new_df[new_df["Salary"]>0])
print("-------")

reset_frame=new_df.reset_index()
print(reset_frame)

new_indices=["Cag","Ahm","Emr","Yiğ"]
new_df["New Indices"]=new_indices
new_df.set_index("New Indices", inplace=True)
print(new_df)

print("---------")
#Multi-index
first_index=["Simpson","Simpson","Simpson","South Park","South Park","South Park"]
inner_index=["Homer","Bart","Marge","Cartman","Kenny","Kyle"]
zipped_index=list(zip(first_index,inner_index))
print(zipped_index)
print("----Zipped Index---")
zipped_index=pd.MultiIndex.from_tuples(zipped_index)
print(zipped_index)

sample_values=np.ones((6,2))
big_df=pd.DataFrame(sample_values, index=zipped_index, columns=["Age","Salary"])
print(big_df)

# !!! print(big_df.loc["Homer"]) buna ulaşamayız çünkü öncesinde simpsona erişmemiz lazım
print(big_df.loc["Simpson"].loc["Homer"])
