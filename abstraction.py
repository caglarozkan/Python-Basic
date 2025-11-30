from abc import ABC,abstractmethod

class Car(ABC):
    
    @abstractmethod
    def maxSpeed(self):
        pass


class Tesla(Car):
    def maxSpeed(self):
        print("200 km")

tesla_car=Tesla()
tesla_car.maxSpeed()

class Mercedes(Car):
    def maxSpeed(self):
        print("300 km")

mercedes_car=Mercedes()
mercedes_car.maxSpeed()
