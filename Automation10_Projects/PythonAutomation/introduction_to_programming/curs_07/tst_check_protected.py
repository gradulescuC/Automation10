from Automation10_Projects.PythonAutomation.introduction_to_programming.curs_07.POO_piloni.tst_encapsulation import Student

class Student_upgraded(Student):
    _var = "test"
    __va1 = "test_private"
    def update_name(self):
         self._name = "Aidan" # Aici variabila nume a fost disponibila in recomandari pentru ca suntem in in interiorul clasei mostenitoare

std = Student
# print(std._name) Aici ne da eroare: AttributeError:
                    # type object 'Student' has no attribute '_name'
                        # pentru ca suntem in afara pachetylui care contine clasa Student
