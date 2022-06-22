model = 123
print(type(model))
print(isinstance(model,(int,float)))
while isinstance(model,(int,float))==True:  # verific daca inputul de la utilizator este un string
    model = input('Invalid value, please try again.')

