def pret_bilet_taxe(valoare_bilet, taxe_aplicabile): #valoare_bilet, taxe_aplicabile = parametri
    taxe_absolute = valoare_bilet * taxe_aplicabile
    return taxe_absolute

def pret_bilet_discount(valoare_bilet, discount):  #valoare_bilet, discount = parametri
    discount_absolut = valoare_bilet * discount
    return discount_absolut

def pret_total_bilet(pret_bilet, taxe_aplicabile, discount): #pret_bilet, taxe_aplicabile, discount = parametri
    pret_bilet = pret_bilet + pret_bilet_taxe(pret_bilet,taxe_aplicabile) - pret_bilet_discount(pret_bilet,discount)
                            #    pret_bilet, taxe_aplicabile = argumente  - pret_bilet, discount = argumente
    return pret_bilet

print(f"pretul total al biletului este {pret_total_bilet(30,0.01,0.1)}")

# priority_boarding = 15
# pret_bilet_si_boarding = priority_boarding + pret_total_bilet(30,0.01,0.1)
# print(pret_bilet_si_boarding)

"""
pe scurt:
ce se pune intre paranteze la definitia functiei este parametru
ce se pune intre paranteze la apelarea functiei este argument
"""

"""

$30
0.01 taxe
0.1 discount

0.01 * 30 = 0.03
0.1*30 = 3 

pret_bilet + pret_bilet_taxe(pret_bilet,taxe_aplicabile) - pret_bilet_discount(pret_bilet,discount)

pret_bilet = valoarea initiala a biletului (fara taxe si fara discount)

pret_bilet_taxe(pret_bilet,taxe_aplicabile) -> calculul valorii taxelor aplicabile, in dolari (rezultatul va fi pentru o valoare de 30 de dolari , 0.03)
pret_bilet_discount(pret_bilet,discount) -> calculul valorii discountului aplicabil, in dolari (rezultatul va fi pentru o valoare de 30 de dolari, 3)

La valoarea initiala a biletului (pret_bilet) am adaugat valoarea totala a taxelor in dolari (adica am apelat functia pret_bilet_taxe ca sa putem sa convertim din procent in dolari) si am scazut valoarea totala a discountului in dolari (adica am apelat functia pret_bilet_discount ca sa putem sa convertim din procent in dolari)

pret_bilet + pret_bilet_taxe(pret_bilet,taxe_aplicabile) - pret_bilet_discount(pret_bilet,discount)
=
30 		   +   			 0.3 							 -       			 3 
"""


pret_bilet = int(input("Introduceti pretul biletului fara taxe si discount: "))
taxe_aplicabile = float(input("Introduceti procentul taxelor aplicabile: "))
discount = float(input("Introdu valoarea discountului aplicabil: "))

taxe_absolute = pret_bilet_taxe(pret_bilet,taxe_aplicabile)
discount_absolut = pret_bilet_discount(pret_bilet,discount)

print(f"Taxele care se aplica la valoarea de {pret_bilet} sunt {taxe_absolute} lei")
print(f"Discountul aplicabil pentru {pret_bilet} este de {discount_absolut}")
print(f"Valoarea biletului dupa aplicarea taxelor de {taxe_absolute} lei"
      f" si respectiv a discountului {discount_absolut} este de "
      f"{pret_total_bilet(pret_bilet,taxe_aplicabile,discount)}")