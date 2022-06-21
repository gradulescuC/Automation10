class Masina:
    # fields/attribute
    culoare = "Galben" #daca dam o valoare default nu mai e nevoie de constructor
    marca = None
    model = None
    viteza = 0

    # constructor
    def __init__(self,model,culoare): # self reprezinta un placeholder pentru viitorul nume al obiectului care se va instantia
                                       # model si culoare reprezinta ARGUMENTELE constructorului si ele vor fi considerate obligatorii la momentul instantierii obiectului
        self.model = model  #  aici vom atribui atributelor clasei valorile date ca si PARAMETRU in interiorul constructorului
                                       # in stanga egalului vor fi intotdeauna atributele clasei care vor trebui initializate, iar in dreapta argumentele constructorului care vor fi stocate in atributele clasei
        self.culoare = culoare
        while type(model) is not str: # verific daca inputul de la utilizator este un string
            input('Invalid value, please try again.') # daca nu este string, promptez utilizatorul sa introduca o noua valoare
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

# instanta_masina1 = Masina() # Am instantiat un obiect al clasei Masina numit instanta_masina1

# Nota: Putem sa consideram ca numele clasei este tipul de data al unui obiect

# print(instanta_masina1)
# print(instanta_masina1.culoare) # Am accesat culorea definita in interiorul clasei
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

if __name__ == "__main__":
    instanta_masina4 = Masina("Golf","Negru")
    instanta_masina5 = Masina("BMW","orange")
    print(instanta_masina4.model, instanta_masina4.culoare)
    print(instanta_masina5.model, instanta_masina5.culoare)

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
#
# for viteza in range (180,100,1):
#     if viteza <=180 and viteza>160:
#      consum = 10
#     elif viteza <=160 and viteza>120:
#         consum = 7
#     elif viteza<=120 and viteza >100:
#       consum = 6
#     else:
#         consum = 5
