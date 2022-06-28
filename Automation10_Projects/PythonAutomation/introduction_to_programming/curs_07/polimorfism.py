#polymorphism - cand exista 2 metode cu acelasi nume dar python stie sa o foloseasca pe cea corecta


# ex de built in polymorphic function
print(len("abc"))
print(len([1, 2, 3, 4]))


# user polymorphic function
def add(x, y, z=0):
    return x + y + z

print(add(2, 3))
print(add(2, 3, 4))


# Polymorphism with class methods
class Romania():
    def language(self):
        print("Romanian")

class USA():
    def language(self):
        print("English")

obj_ro = Romania()
obj_usa = USA()
for country in (obj_ro, obj_usa):
    country.language()

# Polymorphism with Inheritance
class Bird:
    def describe(self):
        print("I'm a bird")

    def fly(self):
        print("Flu Flu! I'm flying")


class Parrot(Bird):
    def talk(self):
        print("I also can talk")


class Penguin(Bird):
    def fly(self): # polymorphism - 2 functii cu acelasi nume - se foloseste cea adecvata - cea din clasa copil
        print("I actually can't fly. But that's ok, I'm dressed stylish.")


random_bird = Bird()
random_bird.describe()
random_bird.fly()
print('------------------------')

polly = Parrot()
polly.describe()
polly.talk()
polly.fly()
print('------------------------')

pingu = Penguin()
pingu.describe()
pingu.fly()
len()