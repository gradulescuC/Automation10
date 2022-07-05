"""
Cerinte:

Clasa pisica
Atribute:
- culoare
- rasa
- varsta


Metode:
- miauna
- alearga
- zgarie
- se joaca
- toarce
"""

class Pisica:
    # atribute/campuri
    culoare = None
    rasa = None
    varsta = None
    stare = "chill"
    stare_de_sanatate = "buna"
    inaltime = 1.60

    def __init__(self,culoare,rasa,inaltime):
        self.culoare = culoare
        self.rasa = rasa
        self.inaltime = inaltime

    def miauna(self):
        print("Miau")

    def alearga(self,soarece):
        if(soarece == True):
            print("alearga")

    def zgarie(self,trasa_de_coada):
        if(trasa_de_coada==True):
            print("hhhhhhhhhhzzzzzz")

    def se_joaca(self):
        print("run for your life")

    def toarce(self):
        if self.stare=='chill':
            print("purrrr")
        else:
            print("hsssssssssssss")


pisica_katia = Pisica("maro","maidaneza",30)
pisica_kedi =  Pisica("alba","maidaneza",35)

pisica_katia.toarce()
print(pisica_katia.culoare)
pisica_katia.culoare="rosu"
print(pisica_katia.culoare)
pisica_katia.stare_de_sanatate = "conjuctivita"
print(pisica_kedi.culoare)
print(pisica_kedi) #-> printeaza <__main__.Pisica object at 0x7fa1cbebaf70>
# pisica_kedi = Pisica("negru","maidaneza") -> aici nu se va actualiza obiectul existent, ci se va crea unul nou
# print(pisica_kedi.culoare)
print(pisica_kedi) # printeaza  <__main__.Pisica object at 0x7fa1cbebaee0>

# Vrem sa schimbam starea pisicii din starea chill in starea agitata
pisica_katia.stare = "agitata"
pisica_katia.varsta = 3

pisica_katia.toarce()