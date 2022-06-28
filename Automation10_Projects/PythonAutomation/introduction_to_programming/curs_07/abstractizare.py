'''
Abstraction from Google
Abstraction is used to hide the internal functionality of the function from the users.
The users only interact with the basic implementation of the function, but inner working is hidden.
User is familiar with that "what function does" but they don't know "how it does."
VS
An Abstract class can contain the both method normal and abstract method.
Abstract methods have no budy, they have just the name and

An Interface contains only abstract methods
'''

from abc import ABC, abstractmethod # avem nevoie de importul acesta pentru abstractizare in python

class Car(ABC): #abstract class contains abstract methods

    @abstractmethod # am folosit un decorator ca sa evidentiem mai bine faptul ca metoda este abstracta
    def accelerate(self): #abstract method = metode fara corp (logica interna)
        pass
        # raise NotImplementedError

    @classmethod
    def stop(self): #poate sa contina si metode normale (care au logica interna)
        print("STOP!")



class Ferrari(Car):
    def accelerate(self):
        print("I'm accelerating from 0 to 100 in 5 seconds")
    def stop(self): # poly
        print("I'm a F, I can't stop")


class Lastun(Car):
    def accelerate(self):
        print("I'm accelerating from 0 to 100 in 15 seconds")


f = Ferrari()
f.accelerate()
f.stop()

l = Lastun()
l.accelerate()
l.stop()


# Interface - toate metodele sunt abstracte (An interface is a completely "abstract class")
# Obliga clasele mostenitoare sa implementeze functiile, e ca o reteta pentru subclase

class Animal(ABC):

    @abstractmethod
    def sound(self):
        raise NotImplementedError

    @abstractmethod
    def sleep(self):
        raise NotImplementedError

# a class implements an interface

class Dog(Animal):
    def sound(self):
        print('Ham Ham!')

    def describe(self):
        print('I have an owner')

    def sleep(self):
        print('ZZZZZZZ')


class Cat(Animal):
    def sound(self):
        print('Miau Miau!')

    def sleep(self):
        print('prrrrr')

    def describe(self):
        print('I own a human')

azorel = Dog()
tom = Cat()
azorel.sleep()
azorel.sound()
azorel.describe()

tom.sleep()
tom.sound()
tom.describe()