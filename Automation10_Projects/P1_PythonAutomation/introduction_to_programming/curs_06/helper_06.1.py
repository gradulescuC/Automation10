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
    varsta= None
    stare = "chill"

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

# pisica_katia = Pisica("maro","maidaneza") - returneaza eroare pentru ca in clasa Pisica nu exista constructor cu parametri
pisica_katia = Pisica() #  am creat un obiect cu numele pisica_katia, care reprezinta o instanta a clasei Pisica
pisica_katia.culoare = "maro"
print(pisica_katia.stare) # Am printat pe ecran starea curenta a pisicii
pisica_katia.toarce() #  am apelat metoda toarce prin intermediul obiectului
pisica_katia.stare = "Agitata" # Am schimbat valoarea atributului stare la "Agitata"