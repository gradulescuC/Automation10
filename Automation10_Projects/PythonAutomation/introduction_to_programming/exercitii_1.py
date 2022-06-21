model = 123
print(type(model))
model = "test"
print(type(model))
while type(model) !="<class 'str'>":  # verific daca inputul de la utilizator este un string
    input('Invalid value, please try again.')