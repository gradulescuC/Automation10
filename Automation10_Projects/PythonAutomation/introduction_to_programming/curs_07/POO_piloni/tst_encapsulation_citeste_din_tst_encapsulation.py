class Student:
    _schoolName = 'XYZ School'  # atribut protected

    def __init__(self, name, age):
        self._name = name
        self.__age = age

std = Student("Swati", 25)
print(std._name) # atributele protected pot sa fie folosite, dar nu apar intre sugestii atunci cand folosim std.
# print(std.__age) Atributele private nu pot sa fie accesate deloc

