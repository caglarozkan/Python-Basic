import pandas as pd
import numpy as np

#Series -> one dimensional labeled array holding data of any type
grades_dict = {
    "Caglar":50,
    "Yusuf": 60,
    "Fatih": 70
}
print(pd.Series(grades_dict))

names = ["Caglar","Yusuf","Fatih"]
grades=[50,60,70]
#print(pd.Series(grades))
#print(pd.Series(names))
print(pd.Series(names,grades))
print("-------------- \n")

#Arithmetic
contest_result1=pd.Series(data=[10,2,65], index=["Caglar","Mehmet","Ali"])
print(contest_result1)
contest_result2=pd.Series(data=[54,76,32], index=["Caglar","Mehmet","Ali"])
print("the result of Caglar:",contest_result2["Caglar"])
final_result=contest_result1 + contest_result2
print(final_result)

print("--------------- \n")
