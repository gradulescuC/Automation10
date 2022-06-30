#inheritance = cand o clasa copil mosteneste o clasa parinte si are acces la toate atributele si metodele ei
class Test:
    testVariable = 0

class Chef(Test): # clasa parinte
    cutite = 1
    def make_salad(self):
        print("salad")
    def make_fries(self):
        print("fries")

class Chef2: # clasa parinte
    short = 2

#clasa copil care mosteneste clasa Chef (se trece intre paranteze numele clasei parinte)
class JapaneseChef(Chef):
    def make_sushi(self):
        print("sushi")

class ItalianChef(Chef, Chef2):
    tava = 1
    def make_pizza(self):
        print("pizza")



newbe = Chef() # pot exista obiecte si de tipul clasei parinte
newbe.make_fries()
print("-------------------------------")
nakamoto = JapaneseChef() # initializam un obiect de tip JapaneseChef
nakamoto.make_sushi()
nakamoto.make_salad()
nakamoto.make_fries()

print("-------------------------------")
mario = ItalianChef()
mario.make_pizza()
print(mario.tava)
