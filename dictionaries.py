dict1={
    "key1":"value1",
    "key2":"value2"
} #Basic Structure

fruit_list=["banana","apple"]
calorie_list=[100,200]

fitness_dict={ "banana":100,
                "apple": 200
                }
print(type(fitness_dict))
print(fitness_dict["banana"])

print(fitness_dict.keys())
print(fitness_dict.values())
fitness_dict["banana"]=250
print(fitness_dict["banana"])

fitness_dict["melon"]=300 #bu şekilde dict'e yeni eleman ekleyebiliyoruz
print(fitness_dict)
print(type(fitness_dict.keys()))
print("---------")

fitness_dict_values_list=list(fitness_dict.values())

mixed_dict={
    "Key1" :10,
    "key2": "200",
    "key3" : 300.0
} #values can be different type

last_dict={
    "k1": 10,
    "k2":[50,60],
    "k3": ["100",200,300,"400"],
    "k4": {
        "a":500,
        "b":600
    }
}# values also can be list or another nested dictionary

print(last_dict["k1"])
print(last_dict["k2"][1])
print(type(last_dict["k3"] [3]))
print(last_dict["k4"]["a"])
print(last_dict["k3"])