#You need to cover different types of birds with one similar and one dissimilar
#characteristic.Use Inheritance if applicable

from abc import ABCMeta,abstractmethod

class Bird(metaclass=ABCMeta):
    def delegate(self):
        self.Dissimilar_Characteristic()
        
    def Similar_Characteristic(self): 
        print("I have two wings,two legs and a beak")

    @abstractmethod
    def Dissimilar_Characteristic(self):
        print("prince by lu")


class Parrot(Bird):
    def Dissimilar_Characteristic(self):
        print("I can talk")

class Penguin(Bird):
    def Dissimilar_Characteristic(self):
        print("I can swim")

class Owl(Bird):
    def Dissimilar_Characteristic(self):
        print("I can see in the dark")

class Hen(Bird):
    def Dissimilar_Characteristic(self):
        print("I can't fly")
        
