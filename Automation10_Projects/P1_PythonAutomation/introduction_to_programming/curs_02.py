"""
Atribuire = proces prin care salvam informatii la adresa de memorie identifica cu un nume al unei variabile,
indiferent de tipul de date al acesteia

Operatorii de asignare sunt: = , += , -= , *= , /=
"""

# A. ASSIGNMENT OPERATORS

x = 3
print(x)
print("-------------------------------------")
x = x+3
print(x)
x += 3
print(x)
print("-------------------------------------")
x = x - 3
print(x)
x -= 3
print(x)
print("-------------------------------------")
x = x*3
print(x)
x *= 3
print(x)
print("-------------------------------------")
x = x/3
print(x)
x /= 3
print(x)
print("-------------------------------------")

# B. ARITHMETICAL OPERATORS

"""
operatorii aritmetici sunt operatori care permit operatii matematice

Exemple de operatori aritmetici: +, -, *, /, % (operatorul modulo), ** (operatorul putere), // (floor division)
"""

print(7//2.5)
print(4+6)
print(10%3) # operatorul modulo returneaza restul impartirii deimpartitului la impartitor -> 3 incape in 10 de 3 ori (3*3 = 9) -> ne ramane 1 unitate
print(2**3) # operatorul putere, care ridica baza la putere -> 2 este ridicat la puterea a 3-a si rezultatul va fi 8


# C. COMPARISON OPERATORS

"""
Operatori prin intermediul carora putem compara doua valori distincte (vor fi foarte utili in cadrul assert urilor)
"""
y = 3
x = 2
print(x==2)  # ATENTIE!! Nu confundati operatorul de atribuire (=) cu operatorul de comparatie (==)
print(x==y)
print(x!=2)  # != este un operator de comparatie care verifica faptul ca operatorul din stanga este diferit de cel din dreapta.
                    # daca cele doua valori sunt diferite, rezultatul evaluarii va fi TRUE
                    # putem sa spunem ca valideaza un fals
print(x!=y)

print(x>2) # > este un operator care evalueaza daca valoarea din stanga este mai mare decat valoarea din dreapta
print(x>y)

print(x<2) # < este un operator care evalueaza daca valoarea din stanga este mai mica decat valoarea din dreapta
print(x<y)

print(x>=2) # >= este un operator care evalueaza daca valoarea din stanga este mai mare sau egala cu valoarea din dreapta
print(x>=y)

print(x<=2) # <= este un operator care evalueaza daca valoarea din stanga este mai mica sau egala cu valoarea din dreapta
print(x<=y)


# # D. LOGICAL OPERATORS
"""
Operatorii logici sunt operatori care sunt folositi pentru a defini evaluari mai complexe
formate din mai multe conditii de evaluare

Operatorii logici sunt:  AND OR NOT
"""



print(x<2 and x<y) # x<2 and x<y este o conditie compusa care instruieste sistemul sa o evalueze
                        #ca fiind adevarata, doar daca ambele conditii simple pe care le contine
                            #sunt evaluate ca fiind adevarate
                                # conditia compusa de mai sus va returna false
print(x==2 and x<y) # Conditia compusa va returna true pentru ca ambele conditii simple sunt evaluate ca si TRUE
print(x==2 and x==y) # Conditia compusa va returna FALSE pentru ca continutul variabilei x nu este identic cu continutul variabilei y


print(x==2 or x<y) # Conditia compusa x==2 or x<y instruieste sistemul sa o evalueze ca fiind adevarata
                        # atata timp cat oricare din conditiile simple sunt evaluate ca fiind adevarate

print(not(x==2 or x<y)) # operatorul NOT este folosit pentru a NEGA rezultatul evaluarii unei expresii

""" 
if(not(isDisplayed()))
        = 
if(isDisplayed()==False)
"""
# y = 3
# x = 2

"""

In general operatorul NOT are prioritate in fata operatorilor OR si AND
Operatorul AND are prioritate in fata operatorului OR


Ordinea prioritatii: NOT > AND > OR

Exemple de evaluari: 

FALSE or FALSE = FALSE
FALSE or TRUE = TRUE
TRUE or TRUE = TRUE

FALSE and FALSE = FALSE
FALSE and TRUE = FALSE
TRUE anf TRUE = TRUE

not FALSE = TRUE
not TRUE = FALSE

Exemple de conditii evaluate: 

print(not x==2 or y>5 and x<y)
    - Ordinea evaluarii va fi: 
            not x==2 (FALSE)
            y>5 and x<y (FALSE)
            FALSE OR FALSE

print(not (x==2 or y>5 and x<y))
    - Ordinea evaluarii va fi: 
            x==2 (TRUE)
            y>5 (doar daca x==2 va fi evaluata ca FALSE)
            x<y (TRUE)
            TRUE or TRUE => TRUE
            not TRUE => FALSE

print(not ((x==2 or y>5) and x<y))
    - Ordinea evaluarii va fi: 
            x==2 (TRUE)
            y>5 (doar daca x==2 va fi evaluata ca si FALSE)
            x<y (TRUE)
            TRUE and TRUE => TRUE
            not TRUE = >FALSE

print(not x==2 or (y>5 and x<y))
    - Ordinea evaluarii va fi:
            not x==2 (FALSE)
            y>5 (FALSE1)
            x<y (doar daca y>5 va fi evaluata ca si TRUE) => TRUE
            FALSE1 and TRUE => FALSE3
            FALSE or FALSE3 => FALSE

not x==2  = A (FALSE)
y>5 and x<y = B (FALSE)
A or B (FALSE or FALSE = FALSE)


"""

print(not(x==2 or x<y))
print(x<y and x>y and x == y)
print(x<y or x>y and x <= y)


# D. FLOW CONTROL

"""
Un flow control este o modalitate prin care putem sa instruim programul sa execute un set de instructiuni
sau un alt set de instructiuni in functie de rezultatul evaluarii unei conditii

Daca conditia este adevarata, atunci se va executa un set de instructiuni
Daca conditia este falsa, atunci se va executa un alt set de instructiuni

Componente ale unei decizii (flow control)
- inceputul deciziei = IF
- ramura din dreapta a deciziei, care se va executa doar atunci cand conditia este evaluata ca fiind adevarata (THEN)
- ramura din stanga a deciziei, care se va executa doar atunci cand conditia este evaluata ca fiind falsa (ELSE)
            ELSE - ul tine loc unui set de instructiuni implicite
- conditie aditionala separata, ca sa sa fie evaluata in cazul in care conditia principala este evaluata ca si falsa (ELIF)



Nota: Noi putem sa adaugam o decizie in interiorul unei alte decizii, caz in care putem sa vorbim despre decizii IMBRICATE
        (Decizii imbricate = Embedded decisions)

- Conditia decizionala este separata de prima instructiune de pe ramura de THEN prin semnul ":"
- Putem sa includem o instructiune in interiorul unei decizii prin indentarea sa fata de marginea din stanga programului
- Sfarsitul if-ului va fi considerat acolo unde este intalnita prima instructiune neindentata
        ATENTIE!!! exceptie va face keyword-ul ELSE

- Ordinea keyword-urilor o sa fie: IF, ELIF, ELSE

"""

"""

Constanta este o adresa de memorie care nu trebuie sa isi schimbe valoarea
In python conceptul de constanta NU exista din punct de vedere tehnic 
        - eu nu pot sa implementez o modalitate de a restrictiona schimbarea unei valori la o adresa de memorie
In python, ca sa putem implementa conceptul de constanta, s-a decis prin conventie ca toate adresele de memorie care nu vrem
            sa isi schimbe continutul sa fie scrise in intregime cu majuscule        

"""

NOTA_DE_TRECERE = 5 # constant that we do not want to change it's value
NOTA_DE_TRECERE_PURTARE = 7

nota_examen = int(input("Introduceti nota de la examen "))
nota_purtare = int(input("Introduceti nota la purtare "))

if nota_examen >= NOTA_DE_TRECERE and nota_purtare >= NOTA_DE_TRECERE_PURTARE:
    print("Am trecut")
    if nota_examen==10 and nota_purtare==10:
        print("felicitari,esti premiant")
else: # Else does not have a condition because it means the instructions to be executed in case the previous condition is evaluated as false
    print("Nu am trecut")
    if(nota_purtare >= NOTA_DE_TRECERE_PURTARE):
        print("Mai invata")
    elif(nota_examen >= NOTA_DE_TRECERE):
        print("Fii cuminte, ca altfel nu vine mosul!")
    else:
        print("Trebuie sa fii mai serios")




optiune = int(input("Alegeti limba, pentru romana apasati 1, pentru engleza apasati 2"))
if optiune == 1:
    print("Ati ales limba romana")
    optiune1 = input("pentru persoane fizice apasati 1, pentru persoane juridice apasati 2")
    if(optiune1 == 1):
        print("Ati ales persoana fizica")
    elif(optiune1 == 2):
        print("Ati ales persoana juridica")
    else:
        print("Optiune invalida, va rugam sa incercati din nou")

elif optiune==2:
    print("You chose english")
    optiune1 = input("For individual persons press one, for companies press 2")
    if (optiune1 == 1):
        print("You chose individual person")
    elif (optiune1 == 2):
        print("You chose a company")
    else:
        print("Invalid option, please try again")
elif optiune == 3:
    print("return to main menu")

else:
    print("Invalid option, please choose another option")


pasaport = input("Aveti pasaport? ")
varsta = input("va rugam sa introduceti varsta persoanei")

if pasaport == 'Da':
    if varsta>=18:
        print("Puteti trece")
    else:
        ambiiParinti = input("Sunt ambii parinti prezenti? Da/NU ")
        if ambiiParinti == 'Da':
            print("Puteti trece")
        else:
            permisiuneParinteLipsa = input("exista permisiune de la parintele lipsa? Da/NU")
            if permisiuneParinteLipsa=='Da':
                print("Puteti trece")
            else:
                print("Nu puteti trece")



pasaport = input("Aveti pasaport? ")
varsta = input("va rugam sa introduceti varsta persoanei")
ambiiParinti = input("Sunt ambii parinti prezent? Da/NU")
permisiuneParinteLipsa = input("exista permisiune de la parintele lipsa? Da/NU")


if pasaport == 'Da' and (ambiiParinti == 'Da' or permisiuneParinteLipsa == 'Da'):
    print("permite calatoria")
else:
    print("nu permite calatoria")
