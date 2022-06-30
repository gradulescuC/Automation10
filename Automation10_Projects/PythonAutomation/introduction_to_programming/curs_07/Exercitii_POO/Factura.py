from datetime import date

from tabulate import tabulate

class Factura:
    seria = 123456

    def __init__(self, numar, nume_produs, cantitate, pret_buc):
        self.numar = numar
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_buc = pret_buc

    def schimba_cantitatea(self, cantitate):
        self.cantitate = cantitate

    def schimba_pretul(self, pret):
        self.pret_buc = pret

    def schimba_nume_produs(self, nume):
        self.nume_produs = nume

    def calc_total(self):
        return self.pret_buc * self.cantitate

    def genereaza_factura(self,lista_prod):
        print(tabulate(lista_prod,
                       headers=['Produs', 'Cantitate', 'Pret Buc', 'Total', 'Data']))


instanta_factura = Factura(121, 'mere', 5, 3)
instanta_factura1 = Factura(121, 'kiwi', 5, 3)
print(f"Seria si numarul facturii pentru {instanta_factura.nume_produs} este {instanta_factura.seria} {instanta_factura.numar}, numar total de produse {instanta_factura.cantitate} la pretul per bucata de {instanta_factura.pret_buc} lei")

instanta_factura.schimba_cantitatea(10)
instanta_factura.schimba_nume_produs("capsuni")

lista_produste = [[instanta_factura.nume_produs,instanta_factura.cantitate,instanta_factura.pret_buc,instanta_factura.calc_total(), date.today()],
                  [instanta_factura1.nume_produs,instanta_factura1.cantitate,instanta_factura1.pret_buc,instanta_factura1.calc_total(),date.today()]]
instanta_factura1.genereaza_factura(lista_produste)