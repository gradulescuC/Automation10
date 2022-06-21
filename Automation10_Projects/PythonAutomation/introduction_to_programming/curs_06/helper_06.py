# from introduction_to_programming.curs_06 import Masina
# masina1 = Masina("Ford",'Fuchsia')
# print(f"Modelul masinii este {masina1.model} si culoarea masinii este {masina1.culoare}")

class Scoala:
    adresa = None
    nr_clase = 0
    nr_elevi_per_clasa = 0

    def calculeazaNrTotalElevi(self,nr_clase,nr_elevi_sc1):
        nr_total_elevi = nr_clase * nr_elevi_sc1
        return nr_total_elevi

scoala1 = Scoala() # Am instantiat un obiect al clasei scoala care va primi in mod implicit atributele si metodele clasei scoala
print(scoala1.adresa)
scoala1.adresa = "Strada floricelelor nr 64, Ferentexas"
nr_clase_sc1 = int(input("Introdu numarul de clase pentru scoala 1"))
nr_elevi_sc1 = int(input("Introdu numarul de elevi pentru scoala 1"))
# nr_total_studenti = scoala1.calculeazaNrTotalElevi(nr_clase_sc1)
print(f"numarul de clase din scoala 1 este {nr_clase_sc1}")
print(f"numarul total de elevi din scoala 1 este {scoala1.calculeazaNrTotalElevi(nr_clase_sc1,nr_elevi_sc1)}")
