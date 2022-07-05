"""
Structuri repetitive  = blocuri de cod care se vor executa in mod repetitiv
    pana cand o anumita conditie nu mai este repectata

Iteratie = procesul prin care un bloc de cod este executat in cadrul structurii repetitive
"""

# print('--------------WHILE/WHILE ELSE---------------------')

"""
while = structura repetitiva care se executa atata timp cat o conditie
este evaluata ca si adevarata
contorul de control al structurii repetitive trebuie declarat in afara structurii repetitive
si modificat in interiorul blocului de cod

Daca nu modificam valoarea contorului in interiorul blocului de cod, atunci vom intra intr-un ciclu infinit
"""

i = 0
while i<=3:
    print(i)
    i+=1  # "+=" este un operator de atribuire care are rolul de a adauga valoarea din dreapta la valoarea
                 # deja existenta in variabila din stanga
print("done")

"""
i = 0 => i<=3? DA print(i)
i = 1 => i<=3? Da print(i)
i = 2 => i<=3? Da print(i)
i = 3 => i<=3? Da print(i)
i = 4 => i<=3? Nu
print("done")
"""

"""
WHILE = tipul structurii repetitive
i<=3: = conditia care se evalueaza
else = setul de instructiuni care se va executa dupa ce se iese din structura repetitiva
"""


# i = 4
# while i<=3:
#     print(i)
#     i = i+1
#     print(i)
# else:
#     print("done")

# debug = depanare -> punem pauza in cod ca sa vedem cum arata o anumita situatie

print('---------------------FOR/FOR ELSE---------------------')

# for i in range(40):
#     print(i)

# range -> range este o functie care defineste un interval
#       De unde incepem, daca nu punem default e 0
#       pana unde? Daca nu punem va fi limita superioara -1
#       pasul - optional
#       capatul superior al intervalului nu este luat in considerare, adica ultima valoare va fi
             # capat superior - 1

# for i in range(1,102, 10): #  1 = inceput interval, 102 = sfarsit interval, 10 = pas
#     print(f"Dalmatianul curent este catelul {i}")

# for i in range(40):
#      print(i)
# else:
#     print(f"La iesire din for i are valoarea {i}")

# # Calculeaza primele 101 numere pare

# for i in range(0,102,2):
#     print(i)


text = 'radar'
text_inversat = ''
for i in range(len(text), 0, -1):
    text_inversat = text_inversat + text[i - 1]
print(text_inversat)



"""

cerinta: 
o sa vrem sa parcurgem lista si sa verificam daca in lista exista valoarea "alb"
Daca exista, vrem sa o stergem din lista, si sa printam urmatorul text:
'Aceasta este o nonculoare, si va fi eliminata din lista'

"""
culori = ["alb","rosu","verde","mov","fuchsia","galben","magenta"]
#
# print(culori)
# for i in range(len(culori)):
#     if culori[i] =='alb':
#         alb = True
#         print("Aceasta este o nonculoare, si va fi eliminata din lista")
#     if culori[i]=="rosu":
#         print("Am gasit si rosu in lista")
# print(f"lista finala este {culori}")
#
# if alb == True:
#     culori.remove("alb")
#
# culori = ['alb','verde','rosu','mov']
#
# print('---------------------FOR EACH---------------------')
#
# # for culoare in list(culori):
# #     if culoare == 'alb':
# #         print('Este non culoare')
# #         culori.remove(culoare)
# # print(f'Lista finala este {culori}')
#
# """
#
# # for i in range(len(culori)): -> 0,1,2,3,4,5,6
# # for culoare in list(culori): -> "alb","rosu","verde","mov","fuchsia","galben","magenta"
#
# For = structura repetitiva evaluata pe baza de index
# for each = structura repetitiva evaluata pe baza de element
#
# """
#
# """
# Exercitiu:
#
# Avem o lista de note si vrem sa calculam media aritmetica a clasei
#
# """
#
# #  Rezolvare cu FOR
#
# lista_note = [10,10,10,9,5,8,9]
# suma = 0
# for i in range(len(lista_note)):
#     suma += lista_note[i]
#
# medie = suma / len(lista_note)
# print(medie)
#
# """
# functionare:
# i = 0 => 0 <7? DA => Suma = 0 + 10 = 10
# i = 1 => 1 < 7? DA => Suma = 10 + 10 = 20
# i = 2 => 2 < 7? DA => Suma = 20 + 10 = 30
# i = 3 => 3 < 7? DA => Suma = 30 + 9 = 39
# i = 4 => 4 < 7? DA => Suma = 39 + 5 = 44
# i = 5 => 5 < 7? DA => Suma = 44 + 8 = 52
# i = 6 => 6 < 7? DA => Suma = 52 + 9 = 61
# i = 7 => 7 < 7? NU
# medie = 61 / 7  = 8.714285714285714
# """
#
# #  Rezolvare cu FOR EACH
#
# for nota in lista_note:
#     suma +=nota
# medie = suma / len(lista_note)
# lista_note = [10,10,10,9,5,8,9]
#
# """
# nota = 10  => suma = 0 + 10 = 10
# nota = 10  => suma = 10 + 10 = 20
# nota = 10  => suma = 20 + 10 = 30
# nota = 9   => suma = 30 + 9 = 39
# nota = 5   => suma = 39 + 5 = 44
# nota = 8   => suma = 44 + 8 = 52
# nota = 9   => suma = 52 + 9 = 61
# """
#
#
# """
# Exercitiu:
#
# Am o lista de masini, si vreau sa ii prezint unui potential client masinile mele, pentru ca el sa poata alege
# ce ii place.
# Criteriile lui sunt sa nu fie masini dacia sau peugeot
# Noi vom scrie o instructiune care sa itereze prin toate masinile, si sa sara peste cele de mai sus
# """
#
# lista_masini = ["BMW","Chevrolet","Lastun","Trabant","Dacia","Peugeout","Oltcit","Audi","Volkswagen","Mercedes"]
#
# for masina in lista_masini:
#     if masina == "Dacia" or masina =="Peugeout":
#         continue
#     print(f"Va recomandam masina {masina}")
#
# """
# masina = BMW => masina == "Dacia" or masina =="Peugeout"? -> Va recomandam masina BMW"
# masina = Chevrolet => masina == "Dacia" or masina =="Peugeout"? -> Va recomandam masina Chevrolet"
# masina = Lastun => masina == "Dacia" or masina =="Peugeout"?  -> Va recomandam masina Lastun"
# masina = Trabant => masina == "Dacia" or masina =="Peugeout"?  -> Va recomandam masina Trabant"
# masina = Dacia => masina == "Dacia" or masina =="Peugeout"?  DA
# masina = Peugeout => masina == "Dacia" or masina =="Peugeout"?  DA
# masina = Oltcit => masina == "Dacia" or masina =="Peugeout"?  Va recomandam masina Oltcit"
# masina = Audi => masina == "Dacia" or masina =="Peugeout"?  Va recomandam masina Audi"
# masina = Volkswagen => masina == "Dacia" or masina =="Peugeout"?  Va recomandam masina Volkswagen"
# masina = Mercedes => masina == "Dacia" or masina =="Peugeout"?  Va recomandam masina Mercedes"
# """
#
#
departamente = {1:{"HR":{1:"Adrian Ioan",
                         2:"Marcel Antonescu",
                         3:"Carmen Dumitrache",
                         4:"Mircea Mateescu"
                         },
                   },
                2:{"IT":{
                         5:"Bogdan Mihalcea",
                         6:"Maria Andronescu",
                         7:"Raluca Balaniuc"
                         }
                   }
                }
#
#
print("Departamentele din companie sunt: ")
for k, v in departamente.items():
    print(*(v.keys()), sep=", ",end=" ")
    print()

# """
# k = 1
# v = {"HR":{1:"Adrian Ioan",
#                          2:"Marcel Antonescu",
#                          3:"Carmen Dumitrache",
#                          4:"Mircea Mateescu"
#                          },
#                    }
# print(*(v.keys()), sep=", ",end=" ") ->  HR
#
# k = 2
# v = {"IT": {
#                          5:"Bogdan Mihalcea",
#                          6:"Maria Andronescu",
#                          7:"Raluca Balaniuc"
#                          }
#                    }
# print(*(v.keys()), sep=", ",end=" ") -> IT
# """
#
# departmentName = input("Introdu numele departamentului pentru care vrei sa afisezi angajatii: ")
# print(f"Angajatii din departamentul {departmentName} sunt:")
# for i, j in departamente.items():
#     for k, v in j.items():
#         if k == departmentName:
#             print(*(v.values()), sep=", ",end=" ")

# """
# departmentName = HR
# i,j in    departamente.items():
# i = 1
# j = {"HR":{1:"Adrian Ioan",
#                          2:"Marcel Antonescu",
#                          3:"Carmen Dumitrache",
#                          4:"Mircea Mateescu"
#                          },
#                    }
# k = HR
# v = {1:"Adrian Ioan",
#                          2:"Marcel Antonescu",
#                          3:"Carmen Dumitrache",
#                          4:"Mircea Mateescu"
#                          }
# if k == HR:  Yes
# print(*(v.values())) -> Marcel Antonescu, Carmen Dumitrache, Mircea Mateescu
# --------------------------
#
# i = 2
# j = {"IT":{
#                          5:"Bogdan Mihalcea",
#                          6:"Maria Andronescu",
#                          7:"Raluca Balaniuc"
#                          }
#                    }
# k == HR? NU -> skip
# """

# Algoritmul de sortare a unei liste prin metoda bulelor

# Varianta cu FOR
numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
print(f'Lista originala este {numere}')
swap = 0
for i in range(len(numere)) :
    for j in range(len(numere) - 1) :
        if numere[j] > numere[j + 1]:
            swap = numere[j]
            numere[j]=numere[j + 1]
            numere[j + 1] = swap
print(f'Lista ordonata este {numere}')
#

# Varianta cu WHILE
print(f'lista nesortata este {numere}')
for j in range(len(numere)):
     swapped = False
     i = 0
     while i<len(numere)-1:
         if numere[i]>numere[i + 1]:
             numere[i], numere[i + 1] = numere[i + 1], numere[i]
             swapped = True
         i = i+1
     if swapped == False:
        break
print (f'lista sortata este {numere}')
