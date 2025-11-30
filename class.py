class Person():
    #property
    #name=""
    #age=0
    #gender=""  #Burada bunları tanımlamamıza da gerek yok aslında çünkü ilerde self ile kullandıgımız için python otomatik olarak algılıyor böyle bi property oldugunu
    job="" #job="developer" yaparsak tanımlanan tüm classlara otomatik olarak atanır

    #initialize method
    def __init__(self,name,age,gender): #class içinde fonksiyon
        print("Init executed..") #constructor gibi burda
        self.name=name #burada self kullanınca ismini ınput gibi yapmamıza gerek yok yine class içindeki variaeble ismini verebiliriz.
        self.age=age
        self.gender=gender
    
    #method
    def test(self):
        print("This is test function for",self.name)

caglar=Person("Caglar",21,"Male")
#caglar.name="caglar ozkan"
#caglar.age=21
#caglar.gender="Male"

emre=Person("Emre",20,"Male")
print(type(emre))
print("Emre'nin yası:",emre.age)

yigit=Person("Yigit",22,"Male")
yigit.test()
yigit.job="Developer"

person_list=[caglar,emre,yigit]
for i in person_list:
    if i.age >=21:
        print(i.name,i.age,i.gender,i.job)
print("------------------")

class Dog():
    year=7
    def __init__(self,age=5): #default olarak da atama yapabiliriz
        self.age=age

    def humanage(self):
        return self.age * Dog.year #Dog.year=self.year (class adı)

    def bark(self):
        if self.age <=2:
            print("Not barking")
        else:
            print("Dog is barking")

myDog=Dog(4)
print(myDog.age)
print(myDog.humanage())

dog2=Dog(1)
dog2.bark()
myDog.bark()