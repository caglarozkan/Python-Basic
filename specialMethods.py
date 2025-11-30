class Fruit():
    def __init__(self,name,calories):
        self.name=name
        self.calories=calories

    def __str__(self): #__str__ kullanarak burada degiştiriyoruz outputu artık bu sayede print(object) sayesinde yazdırma yapabiliriz
        return f"{self.name} : {self.calories} calories"

    def __len__(self):
        return self.calories

myFruit=Fruit("Banana",150)
print(myFruit.name,myFruit.calories)
#print(myFruit)   --> <__main__.Fruit object at 0x00000266E7D46A50> hafızada buraya kaydettim diyor
#peki print(myFruit)  çalışmasını istiyorsak class içinde özel methodları degiştirmemiz lazım
print(myFruit)
print(len(myFruit))