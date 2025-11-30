def divideNumber(number):
    return number/2

print(divideNumber(20))

my_list=[10,34,75,2,65,12,76,121]

myResult_list=[divideNumber(i) for i in my_list ] #list comprehesions
print(myResult_list)

print("------------")

my_list=list(map(divideNumber,my_list)) #mylist içindeki bütün elemanlara divide number fonk uyguluyor ve memory de bir yere kaydediyor bunu da listeye ve ya öyle bir koleksiyona cevirerek ulaşabiliriz
print(my_list)
print("-----------")

def control_string(string):
    return "Caglar" in string 

print(control_string("Caglar"))

myString_list=["Caglar Ozkan","Caglar","Ozkan","Ahmet","Mehmet Caglar"]
myString_list=list(map(control_string,myString_list))#burada artık liste true false içeren bir listeye dönüşüyor çünkü map kullanarak fonksiyon uyguladık ve onları yeni bir liste oluşturduk
print(myString_list)
print("----------")

my_newString=["1","2","3","4","5","11","12","23","61"]

def control_num_string(num_string): #içerisinde 1 stringi içeren ifadeleri kontrol eder
    return "1" in num_string

my_newString=list(filter(control_num_string,my_newString)) #filter ile liste içinde bulunanları ayrı bir liste olarak tutarız
print(my_newString)
print("-----------------")

multiplylambda=lambda num: num *5
print(type(multiplylambda)) #type is function

print(multiplylambda(10))

num_list=[10,543,764,32,76,12,76,21]
new_numList=list(map(lambda num:num/5,num_list)) #lambda bu şekilde de kullanılabilir
print(new_numList)