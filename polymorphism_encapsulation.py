#Polymorphism
class Banana():
    def __init__(self,name):
        self.name=name
        
    def info(self):
        print("banana")
        return f"100 calories {self.name}"
    
class Apple():
    def __init__(self,name):
        self.name=name

    def info(self):
        print("apple")
        return f"150 calories {self.name}"
    
banana=Banana("banana")
banana.info()
apple=Apple("apple")
apple.info()

fruit_list=[banana,apple]
for fruit in fruit_list:
    print(fruit.info())

print("------------------")

#Encapsulation1
class Phone():
    def __init__(self,name,price):
        self.name=name
        self.__price=price #__price yaptıgım için dışarıya kapalı oldu yani degiştirilemez

    def info(self):
        print(f"{self.name} price is: {self.__price}")

    def change_price(self,price):
        self.__price=price

phone_name=input("Enter the phone name:")
phone_price=int(input("Enter the price:"))

my_phone=Phone(phone_name,phone_price)
my_phone.info()
my_phone.price=30000  #bu degiştirmez çünkü class içinde __price yaptıgımız için degiştirilemez oldu dışardan, sadece class içinde degiştirilebilir
my_phone.info()
my_phone.change_price(100)
my_phone.info()