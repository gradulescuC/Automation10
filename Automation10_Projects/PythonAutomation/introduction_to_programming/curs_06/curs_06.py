"""
 Programare orientata pe obiecte reprezinta o modalitate prin care noi putem templetiza
atributele si comportamentul unui anumit element. 

 Programarea orientata pe obiecte este prescurtata cu acronimul POO sau varianta in engleza
OOP  object oriented programming

 O clasa in general este unul din elementele de baza al programarii orientate pe obiecte
si reprezinta tiparul in sine

 O clasa reprezinta un tipar, dar nu va fi util pana cand nu va fi apelat
 Folosirea unei clase se poate face prin intermediul unui obiect
 Un obiect este o reprezentare efectiva a unei clase
 Crearea unui obiect se numeste instantiere, motiv pentru care, prin definitie,
        un obiect se spune ca este o instanta a unei clase
 In momentul in care cream un obiect, noi vom avea acces prin intermediul lui
        la toate atributele si metodele clasei
 O metoda este o functie definita in interiorul clasei 

                
Exemplu: Clasa masina
Cand definim o clasa ne gandim ce atribute poate sa aiba elementul
si ce actiuni poate sa faca

O masina de exemplu poate sa aiba urmatoarele atribute:
 culoare
 viteza
 an_fabricatie
 marca
 model
 capacitate_rezervor
 tip_combustibil
 tractiune
 serie_sasiu
 cutie_viteze
 numar_inmatriculare

O masina poate sa faca urmatoarele actiuni
 pornire de pe loc
 oprire
 accelerare
 franare
 consum_instant 
 revizie_tehnica (daca masina este in stare buna, trece revizia tehnica)
 schimbare_directie
 vopsire_masina

"""

"""
Definirea clasei se face prin intermediul keywordului "class"
De regula, prin conventie, numele unei clase va incepe cu litera mare si va fi scris in format
        camelCase sau snake_case (de regula snake_case in python)
La fel ca la structurile alternative (IF) si cele repetitive (WHILE, FOR), corpul unei clase este definit
        de indentarea codului, adica lasarea unui spatiu intre marginea fisierului si cod
        
Constructor = un agent care este responsabil cu crearea obiectului
In orice limbaj de programare POO exista un constructor implicit si un constructor explicit

Constructorul explicit este cel care se defineste de catre dezvoltator in cod
Constructorul implicit este cel care se apeleaza automat de python atunci cand constructorul explicit nu este definit

Constructorul este o functie/metoda specifica unei clase care are rolul de a crea obiectul in sine
Constructorul se defineste cu numele __init__ si intre paranteze se vor specifica atributele
        care vrem sa existe in mod obligatoriu la crearea obiectului
        Daca nu se specifica niciun parametru, atunci toate atributele vor fi optionale

In general, intr-o clasa, atunci cand vrem sa accesam elemente definite in interiorul clasei 
        fie ele atribute sau metode, ele trebuie accesate cu elementul "self."
"""
class Masina:
    # fields/attribute
    model = None
    culoare = "Galben" #  Negru
    marca = None
    viteza_max = 0
    an_fabricatie = 0
    capacitate_rezervor = 40
    tip_combustibil = "motorina"
    tractiune = "fata"
    serie_sasiu = None
    cutie_viteze = "manuala"
    numar_inmatriculare = None
    consum_viteza_max = None
    consum_interactiv = None


    def __init__(self, model,culoare): # self reprezinta un placeholder pentru viitorul nume al obiectului care se va instantia
                                       # model si culoare reprezinta ARGUMENTELE constructorului si ele vor fi considerate obligatorii la momentul instantierii obiectului
        self.model = model  #  aici vom atribui atributelor clasei valorile date ca si PARAMETRU in interiorul constructorului
                                       # in stanga egalului vor fi intotdeauna atributele clasei care vor trebui initializate, iar in dreapta argumentele constructorului care vor fi stocate in atributele clasei
        self.culoare = culoare
        # while type(model) is not "str": # verific daca inputul de la utilizator este un string
        #     input('Invalid value, please try again.') # daca nu este string, promptez utilizatorul sa introduca o noua valoare
        if culoare == 'orange': # verificam daca culoarea data ca si argument in constructor este orange
            self.culoare = 'portocaliu' # daca este orange, o schimbam in portocaliu pentru ca nu avem culoarea orange in baza de date

    #metode
    def accelerate(self, viteza): # argumentul self este obligatoriu pentru ca tine loc de numele obiectului care inca nu este definit
                                        #argumentul viteza este dat ca si parametru si care va fi instantiat diferit in functie de obiectul nostru
        return f'Trebuie sa acceleram cu {viteza} de km' # avem nevoie de return in cazul asta specific pentru ca mai jos am folosit in print rezultatul functiei

    def paint(self, colour):
        self.culoare= colour

    def start_masina(self):
        print("Start masina")

    def calcul_consum_interactiv(self,viteza):
        for viteza in range(180, 100, 1):
            if viteza <= 180 and viteza > 160:
                self.consum_interactiv = 10
            elif viteza <= 160 and viteza > 120:
                 self.consum_interactiv = 7
            elif viteza <= 120 and viteza > 100:
                 self.consum_interactiv = 6
            else:
                 self.consum_interactiv = 5
        return self.consum_interactiv

    def calcul_consum_max(self):
            if self.viteza_max <= 180 and self.viteza_max > 160:
                    self.consum_viteza_max = 10
            elif self.viteza_max <= 160 and self.viteza_max > 120:
                    self.consum_viteza_max = 7
            elif self.viteza_max <= 120 and self.viteza_max > 100:
                    self.consum_viteza_max = 6
            else:
                    self.consum_viteza_max = 5
            return self.consum_viteza_max

"""
instantierea unui obiect se face pe baza numelui clasei
Putem modifica alti parametri, sau chiar pe cei definiti prin constructor, dupa instantiere
IMPORTANT:
Orice atribut sau functie din interiorul clasei se poate accesa DOAR prin intermediul obiectului
"""
instanta_masina_bmw = Masina("X5","orange") # Am instantiat un obiect al clasei Masina numit instanta_masina1
print(instanta_masina_bmw.culoare)
instanta_masina_bmw.viteza_max = 120
instanta_masina_volkswagen = Masina("Volkswagen","negru")
instanta_masina_volkswagen.viteza_max = 180
instanta_masina_golf = Masina("Golf","Albastru")
instanta_masina_golf.viteza_max = 180

# instanta_masina_bmw.model = "BMW" # am modificat atributul model si i-am dat valoarea BMW
# instanta_masina_volkswagen.culoare = "Rosu"
# print(instanta_masina_bmw.culoare) # Am accesat culorea definita in interiorul clasei
# print(instanta_masina_volkswagen.culoare)
# print(instanta_masina_volkswagen.model)

# Nota: Putem sa consideram ca numele clasei este tipul de data al unui obiect

# print(instanta_masina1)
# instanta_masina1.culoare = 'Rosu'  # Am modificat culoarea masinii, dar doar pentru prima masina, nu si pentru a doua
# print(f"Culoarea pentru prima masina este {instanta_masina1.culoare}")
# instanta_masina2 = Masina()
# print(f"Culoarea pentru a doua masina este {instanta_masina2.culoare}")
# print(type(instanta_masina1))  #  printeaza valoarea <class '__main__.Masina'>
#
# instanta_masina2.marca = 'Volkswagen'
# instanta_masina1.marca = 'BMW'
# instanta_masina2.model = 'Golf'
# instanta_masina2.viteza = 30
# print(instanta_masina2.viteza)
# print(instanta_masina1.viteza)
#
# print(f"Masina 2 este un {instanta_masina2.marca} {instanta_masina2.model} {instanta_masina2.accelerate(instanta_masina2.viteza)} ")
# instanta_masina1.start_masina()
#
# if __name__ == "__main__":
#     instanta_masina4 = Masina("Golf","Negru")
#     instanta_masina5 = Masina("BMW","orange")
#     print(instanta_masina4.model, instanta_masina4.culoare)
#     print(instanta_masina5.model, instanta_masina5.culoare)

"""

Clasa = tipar pe baza caruia ne putem defini obiecte
obiect = instanta a unei clase (adica reprezentare reala a clasei)
atribute = proprietati pe care le pot avea obiectele
metode = actiuni pe care le pot face obiectele
atributele si metodele pot fi accesae DOAR prin intermediul unui obiect instantiat

"""

# for i in range (180,100,10):
#     if i <=180 and i >100:
#         consum = 10
#     else:
#         consum = 5

# consumul la 180km/h este de 10l
# consum la sub 100km/h este de 5l


# Calcul consum in functie de viteza in afara clasei
for instanta_masina_bmw.viteza in range (180,100,1):
    if instanta_masina_bmw.viteza <=180 and instanta_masina_bmw.viteza>160:
     consum = 10
    elif instanta_masina_bmw.viteza <=160 and instanta_masina_bmw.viteza>120:
        consum = 7
    elif instanta_masina_bmw.viteza<=120 and instanta_masina_bmw.viteza >100:
      consum = 6
    else:
      consum = 5

# lista_masini = [instanta_masina_bmw,instanta_masina_volkswagen,instanta_masina_golf]
# for masina in lista_masini:
#     if masina.viteza_max == 180 and masina.consum_viteza_max == 10:
#         print(f"Va recomandam masina {masina}")