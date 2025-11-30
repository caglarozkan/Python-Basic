#Inheritance,Polymorphism,Abstraction,Encapsulation
class Musician():
    def __init__(self,name):
      print("Musician class created..")
      self.name=name
    
    def test1(self):
       print("test1")

    def test2(self):
       print("test2")

caglar=Musician("Caglar")
caglar.test1()

class MusicianPlus(Musician):  #Inheritance burada Musician ın içerigine erişebiliyoruz
    def __init__(self,name):
      Musician.__init__(self,name)
      print("MusicianPlus .createad..")
    
    def test3(self):
      print("test3")

    def test1(self): #OVERRIDE üstüne yazıyoruz bu fonksiyonu artık bu classın içinde bu yenilenmiş haliyle çalışacak
       print("test1 test1 test1")

ahmet = MusicianPlus("Ahmet")
ahmet.test2()
ahmet.test3()
#caglar.test3() #caglar test3 e erişemez çünkü o ana classın objesi fakat method ınherited classın methodu
#musician classı musicianplus'a erişemez ancak musicianplus musician'a erişebilir
caglar.test1() #bu musician içindeki test1'e erişiyor
ahmet.test1() #bu override edilmiş methoda erişiyor
