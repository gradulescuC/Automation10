from abc import ABC, abstractmethod


class Angajat(ABC):
    @abstractmethod
    def pontaj(self):
        pass

    @abstractmethod
    def testAlcool(self):
        raise NotImplementedError

class AngajatSRI(Angajat):
    __numeProiectAlpha = "Cod Secret Vulturul"
    nume_vechi=[]
    def __init__(self,nume_proiect):
        __numeProiectAlpha = nume_proiect

    def pontaj(self):
        frecventaPontareLuna = 1
        return frecventaPontareLuna

    def testAlcool(self):
        frecventaTestAlcool = 8
        return frecventaTestAlcool

    def ascultaTelefoane(self):
        tipTelefoaneDeAscultat = 'Smartphone'
        return tipTelefoaneDeAscultat

    @property
    def numeProiectAlpha(self):
        return self.__numeProiectAlpha

    @numeProiectAlpha.getter
    def numeProiectAlpha(self):
        print(f"Numele proiectului este {self.__numeProiectAlpha}")
        print(f"Shhhhh, nu mai spune la nimeni")
        return self.__numeProiectAlpha


    @numeProiectAlpha.setter
    def numeProiectAlpha(self,nume_nou):
        try:
             if(nume_nou not in ("asculta","citeste","colecteaza")):
                 self.nume_vechi.append(self.__numeProiectAlpha)
                 self.__numeProiectAlpha = nume_nou
                 print(self.__numeProiectAlpha)
             else:
                 raise NameError("Numele nu este sigur")
        except:
            print("Numele proiectului trebuie definit corect")

    @numeProiectAlpha.deleter
    def numeProiectAlpha(self):
        self.__numeProiectAlpha = None

    # def adauga_nume(self,nume_vechi):
    #     nume_vechi.append(self.__numeProiectAlpha)
    #     print(nume_vechi)


angajatSRI1 = AngajatSRI("Codul Alpha")
# angajatSRI1.pontaj()
# print(angajatSRI1.ascultaTelefoane())
# angajatSRI1.numeProiectAlpha
angajatSRI1.numeProiectAlpha="Codul Secret Intre Alex si David"
# angajatSRI1.numeProiectAlpha
# del angajatSRI1.numeProiectAlpha
# angajatSRI1.numeProiectAlpha
angajatSRI1.numeProiectAlpha = "Cod Secret"
angajatSRI1.numeProiectAlpha = "Cod Si mai Secret"
print(angajatSRI1.nume_vechi)

