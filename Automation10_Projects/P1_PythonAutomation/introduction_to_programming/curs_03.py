#   # Liste
nume = "Michael"
len(nume)  #Va returna 7, pentru ca nume are 7 caractere
print(nume[0:2])  #Va acoperi primele doua caractere din string, pentru ca la slicing capatul superior de interval nu se ia in considerare


"""

1. Identificarea elementelor in liste si slicing pe liste

"""
nume_as_list=['M','i','c','h','a','e','l']  #in cazul asta ar avem o lista cu 7 elemente, fiecare element reprezentant o litera
print(nume_as_list[0]) # va returna M, pentru ca la liste indicele incepe de la pozitia 0.
                        # indexul pe care vreau sa il accesez va fi pus intre paranteze patrate
print(len(nume_as_list))
print(nume[0:2])  #  aici mi se vor afisa doua caractere independente pentru ca eu accesez un string
print(nume_as_list[:2]) #  aici mi se vor afisa doua elemente intr-o lista, pentru ca eu accesez o lista


"""

2. Identificarea indexului la care se afla un element in lista

Cerinta: vreau sa printez pe ecran: "Vreau sa accesez masina Trabant si o voi gasi la indexul 0"
indexul se va extrage prin functie.
"""

masini = ["Trabant","Limuzina","BMW","Volkswagen","Opel","Skoda","Chevrolet","Cadillac"]


print(f"Vreau sa accesez masina Trabant si o voi gasi la indexul {masini.index('Trabant')}")
print(f"Vreau sa accesez masina Skoda si o voi gasi la indexul {masini.index('Skoda')}")

print("----------------------")


"""

3. Cum scoatem un caracter dintr-o lista? Ne putem folosi de functia remove sau pop

"""
print(nume_as_list)
literaRemove = nume_as_list.remove('c')  # Remove poate sa scoata un caracter din lista pe baza codului ASCII (pe baza caracterului in sine)
literaPop = nume_as_list.pop(5) # Pop poate sa scoata un caracter din lista pe baza indexului
print(literaRemove) # va printa None pentru ca functia remove al carei rezultat a fost salvat in variabila literaRemove nu are optiune de return
print(literaPop)  # va printa litera pe care a eliminat-o
print(nume_as_list) # Va printa pe ecran Mihal in urma scoaterii caracterelor e si c



"""
4.  Cum suprascriem?

suprascrierea reprezinta inlocuirea unui caracter la o anumita pozitie cu un alt caracter
suprascrierea se poate face prin intermediul identificarii elementului pe baza de index si prin intermediul operatorului de atribuire

"""

# lista cu care am ramas in urma schimbarilor de mai sus este ['M', 'i', 'h', 'a', 'e']

nume_as_list[0] = 'a' # nume_as_list[0] este identificarea elementului pe baza de index, "=" reprezinta operatorul de atribuire
                            # si 'a' reprezinta carecterul care va inlocuitor la indexul identificat
print(nume_as_list) # ['a','i','h','a','e']

nume_as_list[0] = 'r'
print(nume_as_list)

# nume_as_list['r'] = 'M' - Nu putem sa accesam elementul pe baza de ASCII
# print(nume_as_list)


"""

5. Cum adaugam la index?

# lista cu care am ramas in urma schimbarilor de mai sus este ['r', 'i', 'h', 'a', 'e']

1. Cerinta: Vrem sa inseram o noua litera la inceputul listei astfel incat sa obtinem lista  ['m','r', 'i', 'h', 'a', 'e']
2. Cerinta: Vrem sa inseram o noua litera in pozitia 1 a listei astfel incat sa obtinem lista  ['m','a','r', 'i', 'h', 'a', 'e']

"""

nume_as_list.insert(0,'m')
print(f"Am indeplinit cerinta 1 si am obtinut urmatoarea lista: {nume_as_list} ")
nume_as_list.insert(1,'a')
print(f"Am indeplinit cerinta 2 si am obtinut urmatoarea lista: {nume_as_list} ")


"""
6. Cum adaugam la final?

1. Cerinta: Vrem sa adaugam un nou caracter la finalul listei astfel incat sa obtinem lista ['m','a','r', 'i', 'h', 'a', 'e','n']
2. Cerinta: Vrem sa adaugam un nou caracter la finalul listei astfel incat sa obtinem lista ['m','a','r', 'i', 'h', 'a', 'e','n','a']



"""
nume_as_list.append('n')
# nume_as_list.insert(len(nume_as_list),'n')
print(nume_as_list)
nume_as_list.append('a')
print(nume_as_list)


"""

7. Exercitiu: 

Cum pot sa fac sa elimin din lista caracterul h si caracterul e? 
Cum pot sa fac sa adaug dupa litera i elementele j si u?

"""

nume_as_list.remove('h')
nume_as_list.pop(5)
print(nume_as_list)
nume_as_list.insert(nume_as_list.index('i')+1,'j')
print(nume_as_list)

"""
['m', 'a', 'r', 'i', 'a', 'n', 'a'] => Asta a fost lista de la care am plecat
['m', 'a', 'r',  'j', 'i', 'a', 'n', 'a'] => Asta ar fi rezultat daca am fi scris nume_as_list.insert(nume_as_list.index('i'),'j')
['m', 'a', 'r', 'i', 'j','a', 'n', 'a'] => Asta a fost lista la care am ajuns
  0    1    2    3    4   5    6   
"""


"""

8. Putem pune o lista in alta lista?
Da. Putem prin intermediul conceptului de matrice, sau lista bidimensionala (conceptul de matrice este putin impropriu spus)

lista_in_lista = [
     [1,2,3],
     [4,"", 6],
     [7,8,9],
     [0]
]

"""
lista_in_lista_v1 = [
     [1,2,3],
     [],
     [7,8,9],
     [0]
]

lista_in_lista_v2 = [
     [1,2,3],
     [4,"",6],
     [7,8,9],
     [0]
]

lista_in_lista_v3 = [
     [1,2,3],
     [4,5,6],
     [7,8,9],
     [0]
]
print(lista_in_lista_v1)
print(lista_in_lista_v2)
print(lista_in_lista_v3)

 # cum afisez 7?
print(lista_in_lista_v3[2])
print(lista_in_lista_v3[2][0])

randul3 = lista_in_lista_v3[2]
print(randul3[0])

# luam la intamplare o valoare
# lista2 = ["tel1","tel2","tel3"]
# import random
#    # definesc indexul
# random_nr = random.randint(0, len(lista2))
#    # aleg telefonul
# print(lista2[random_nr])

# print("----------------------------------------")
#
"""
Set - avem valori unice
Setul reprezinta un set de date in care nu sunt permise valori duplicate
Setul se reprezinta, spre deosebire de liste, intre doua acolade
Setul NU este o structura de date ordonata, deci nu va putea fi identificat prin index
"""
vocale = {'a','e','i','o','u'} # am definit un set care sa contina doar vocale
print(vocale)
# print(vocale[0]) # Imi va da eroare -  TypeError: 'set' object is not subscriptable
                        # Eroarea apare pentru ca seturile nu reprezinta o structura de date ordonata
                            # Asta inseamna ca elementele nu pot fi identificabile pe baza de index

# print(vocale["a"])

before = vocale # am stocat setul vocale inainte de modificare intr-o variabila numita before
vocale.add('a')
after = vocale
print(before, after) # am stocat setul vocale dupa modificare intr-o variabila numita after

# Am stocat setul complet inainte si dupa modificare pentru a arata ca setul nu este afectat de modificare
                # daca variabila pe care incercam sa o inseram este un duplicat

if before==after:   #  Am verificat daca valoarea setului inainte si dupa modificare este aceeasi
     print("Ai adaugat un duplicat")

     # ATENTIE! La adaugarea duplicatului NU NE DA EROARE

litera = 'e'
if litera in vocale:
 print("litera e vocala")
else:
 print("litera e consoana")

# putem adauga un nou caracter in set cu functia add
print(f"Vocalele inainte de adaugare: {vocale}")
vocale.add('A')  #  valoarea se va adauga pentru ca este scrisa cu litera mare
                        # codul ASCII al literei 'A' este 65 si al literei 'a' este 97
after = vocale
lungime = len(vocale)
print(f"Vocalele dupa adaugare: {after}. Setul are lungimea de {lungime}")

print("----------------------------------------")

"""
tuplu - este o structura de date ordonata (adica o structura de date in care pot sa accesez elementele pe baza de index)
               care are proprietatea de a fi imutabil (immutable), 
               adica o data definit nu se mai poate schimba (adauga sau sterge valori) 
- permite duplicate

ex: un tuplu cu o echipa de campionat de sah pentru care au fost alesi trei elevi, 
     si e posibil ca doi din ei sa aiba acelasi nume
     
Functii disponibile pentru tupluri: index, count

Tuplurile se pot defini prin intermediul parantezelor rotunde
"""
camere_hotel = (1,2,3,4,5,6,7)
print(camere_hotel[1])
print(camere_hotel)
print(camere_hotel.count(7))  # verifica de cate ori apare un numar intr-un tuplu
print(camere_hotel.index(7))
print(len(camere_hotel))
camere_hotel = (5,7,1,6,8)
print(camere_hotel)


"""
dictionar - este o structura de date definita sub formatul cheie-valoare
In general cheile sunt definite in mod unic si nu se pot schimba sau duplica
Incercarea schimbarii numelui unei chei va duce de fapt la adaugarea unei noi perechi cheie-valoare
Se pot modifica in schimb valorile cheilor
Dictionarele se pot defini prin intermediul acoladelor
"""

# Mai jos am definit un dictionar in care am incercat sa mapam fiecare tara cu capitala proprie
capitale = {
     'Romania':'Bucuresti',
     'Ungaria':'Budapesta',
     'Italia':'Roma',
     'Bulgaria':'Sofia'}

# putem sa accesam date?
# R: DA, se pot accesa datele prin intermediul cheilor sau prin intermediul functiei get
print(capitale['Romania'])
print(capitale.get('Romania'))

# putem sa actualizam o informatie?
# R: Da, se pot actualiza prin intermediul cheilor si al operatorului de atribuire
               # sau prin intermediul functiei update
capitale['Romania'] = 'Cluj'
capitale.update({'Romania':'Alba'})
print(capitale)

# ATENTIE!! instructiunea de mai jos adauga o noua pereche cheie:valoare, NU va actualiza cheia existenta
capitale['Elvetia'] = 'Alba'
print(capitale)

# putem sa adaugam o informatie?
# R: Da, prin intermediul cheilor si al operatorului de atribuire
capitale['Ucraina'] = 'Kiev'
print(capitale)

# putem sa stergem o informatie? # R: Da, prin intermediul functiei pop
capitale.pop('Romania')
print(capitale)

# capitale.pop('Alba') -> Instructiunea asta va returna eroare:  KeyError: 'Alba'
                         # Eroarea va fi returnata pentru ca nu exista cheia 'Alba' in dictionar
# print(capitale)

# Putem sa concatentam doua dictionare? Da, prin intermediul functiei update
capitale2={'Liechtenstein':'Vaduz','Cehia':'Praga'}
capitale.update(capitale2)
print(capitale)

capitale3 = {'Italia':'Milan'}
capitale.update(capitale3)
print(capitale)

# Putem sa afisam doar CHEILE unui dictionar? R: Da, prin intermediul functiei 'keys'
print(capitale2.keys())
print(capitale.keys())

# Putem sa afisam doar VALORILE unui dictionar? R: Da, prin intermediul functiei 'keys'
print(capitale.values())


# Putem sa afisam perechile CHEIE-VALOARE ale unui dictionar? R: Da, prin intermediul functiei 'keys'
print(capitale.items())

dictionar_orase = {
     1:"Brasov",
     2:"Bucuresti"
}

print(dictionar_orase.keys())
print(dictionar_orase.values())
print(dictionar_orase.items())
print(dictionar_orase)

