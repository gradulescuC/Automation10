lista_numere = [1, -2, 3, 8, 0, -5]

def returnare_pozitiva(lista_numere):
    for numar in lista_numere:
        if numar <= 0:
            lista_numere.remove(numar)
    print(lista_numere)

def numere(lista):
    for i in lista:
        if i<=0:
            lista.remove(i)
lista=[5, 7, 3, 9, -3, 3, -1, 0, -4, 3]
numere(lista_numere)
print(lista_numere)
