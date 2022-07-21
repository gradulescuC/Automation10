#inheritance = cand o clasa copil mosteneste o clasa parinte si are acces la toate atributele si metodele ei


class Chef(): # clasa parinte
    cutite  = None
    def __init__(self,nr_cutite):
        self.cutite = nr_cutite

    def make_salad(self):
        print("salad")
    def make_fries(self):
        print("fries")

class Chef2: # clasa parinte
    short = 2

#clasa copil care mosteneste clasa Chef (se trece intre paranteze numele clasei parinte)
class JapaneseChef(Chef):
    def __init__(self,cantitate_alge,cutite):
        self.alge = cantitate_alge
        self.cutite = cutite

    def make_sushi(self):
        print("sushi")

class ItalianChef(Chef, Chef2):
    tava = 1
    def make_pizza(self):
        print("pizza")



newbe = Chef() # pot exista obiecte si de tipul clasei parinte
newbe.make_fries()
print("-------------------------------")
nakamoto = JapaneseChef(5,3) # initializam un obiect de tip JapaneseChef
nakamoto.make_sushi()
nakamoto.make_salad()
nakamoto.make_fries()

print("-------------------------------")
mario = ItalianChef()
mario.make_pizza()
print(mario.tava)
