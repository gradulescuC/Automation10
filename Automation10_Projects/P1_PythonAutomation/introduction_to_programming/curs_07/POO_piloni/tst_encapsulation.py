class Student:
    _schoolName = 'XYZ School'  # atribut protected
    __schoolNamePrivate = "Test"

    def __init__(self, name, age):
        self._name = name
        self.__age = age

std = Student("Swati", 25)
print(std._schoolName) # atributele protected pot sa fie folosite, dar nu apar intre sugestii atunci cand folosim std.
# print(std.__age) Atributele private nu pot sa fie accesate deloc
print(std._schoolName)
# print(std.__schoolNamePrivate) - Va returna eroare: AttributeError: 'Student' object has no attribute '__schoolNamePrivate'