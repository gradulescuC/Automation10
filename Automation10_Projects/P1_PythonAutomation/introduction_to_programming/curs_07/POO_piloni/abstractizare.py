'''
Abstractozarea este un proces prin care putem sa ascundem o anumita functionalitate specifica fata de un utilizator
            si de asemenea de a putea forta un anumit comportament in clasele mostenitoare
Utilizatorul stie ce face functionalitatea, dar nu si cum o face

Cand vorbim despre abstractizare exista doua concepte:
- Clasa abstracta - contine atat functii abstracte cat si functii proprii, definite
- Interfata - contine doar functii abstracte

O metoda abstracta este o metoda care nu are corp

'''

from abc import ABC, abstractmethod # avem nevoie de importurile acestea pentru abstractizare in python

class Car(ABC): # Am definit clasa Car care mosteneste conceptul de abstractizare (fara mostenirea asta nu o putem face abstracta)

    @abstractmethod # am folosit un decorator ca sa marcam metoda ca abstracta
    def accelerate(self): # am inceput definirea metodei abstracte = metode fara corp (logica interna)
        # in general metodele abstracte nu trebuie sa aiba logica, si atunci pentru a nu avea erori avem doua optiuni:
        pass   # scriem pass
        # raise NotImplementedError - ridicam o exceptie de NotImplemented

    @classmethod
    def stop(self): # O clasa abstracta poate sa contina si metode normale (care au logica interna)
        print("STOP!")  #  metodele de clasa, cu logica, nu este obligatoriu sa fie implementate in clasele mostenitoare
                                # decoratorul classmethod e optional, dar de regula il punem pentru claritate


# Aici am definit o clasa noua numita Ferrari care mosteneste clasa abstracta Car, ceea ce inseamna ca noi vom fi
                        # fortati sa implementam metoda abstracta accelerate
class Ferrari(Car):
    def accelerate(self):  # daca nu am avea metoda asta definita, am primi o exceptie de tip NotImplementedError
        print("I'm accelerating from 0 to 100 in 5 seconds")  # puteti sa incercati sa o comentati sa vedeti ce se intampla

    def stop(self): # poly
        print("I'm a F, I can't stop")

# Am implementat din nou o clasa care mosteneste clasa abstracta Car. Aici de asemenea suntem obligati sa implementam metoda accelerate

class Lastun(Car):
    def accelerate(self):
        print("I'm accelerating from 0 to 100 in 15 seconds")


f = Ferrari()
f.accelerate()
f.stop()

l = Lastun()
l.accelerate()
l.stop()


# Mai jos am definit o Interfata - adica o clasa abstracta in care toate metodele sunt abstracte (An interface is a completely "abstract class")
# Obliga clasele mostenitoare sa implementeze functiile, e ca o reteta pentru subclase

class Animal(ABC): # ABC  =  Abstract Base Class

    @abstractmethod  # decorator care marcheaza metoda ca fiind abstracta
    def sound(self):
        raise NotImplementedError

    #  pass = cuvant cheie care defineste faptul ca corpul metodei nu are o logica efectiva, dar este folosit pentru ca acea metoda
         # sa poata sa aiba un corp
    #  raise NotImplementedError = modalitate prin care putem sa fortam in mod explicit exceptia de not implemented

    def sleep(self):
        print('zzzzzzzz')

# Atunci cand o clasa mosteneste o alta clasa de tip interfata sau clasa abstracta, spunem ca o implementeaza

class Dog(Animal):

    def sound(self):
        print('Ham Ham!')

    def describe(self):
        print('I have an owner')


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