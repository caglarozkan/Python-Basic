import pandas as pd

df=pd.read_csv("8-apply_function_data.csv")
print(df)
#print(df.describe())


#----  APPLY ----
print("-------------")
def salary_category(salary):
    if salary < 50000:
        return "Low"
    elif salary>=50000 and salary < 80000:
        return "Medium"
    else:
        return "High"

df["Salary Category"]=df["Salary"].apply(salary_category) #salary column'una salary category fonksiyonunu cagırarak yeni bir columna atadık
print(df)

print("-----------")
def adjust_performance(experience):
    if experience > 10:
         return 1
    else:
        return 0

df["Adjusted"] = df["Experience"].apply(adjust_performance)
print(df)
df["New Performance Score"]=df["Performance_Score"]+df["Adjusted"]
print(df)

print("-----------")
def adjusted_new(row):
    if row["Experience"] > 10:
        return row["Performance_Score"]+1
    else:
        return row["Performance_Score"]

df["Adjusted_New"]= df.apply(adjusted_new, axis=1)
print(df)

print("-----------")
#lamdba kullanarak da yapabiliriz
df["Formatted_Name"]=df["Name"].apply(lambda x : x.replace("_","")) # _ olan yerleri (bosluk)  ile doldur
print(df)