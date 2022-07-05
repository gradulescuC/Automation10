class company():
    departamente = {}
    angajati = {}

    def __init__(self, fname, lname, age, job, salary):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.job = job
        self.salary = salary

    def applyBonus(self, value):
        self.salary += value

    def add_department(self, departmentId, departmentName):
        self.departamente[departmentId] = departmentName

    def add_employee_to_department(self, employeeId, employeeName, departmentName):
        self.angajati[employeeId] = {employeeName:departmentName}

    def display_employees(self,departmentName):
        print(f"The employees in the department {departmentName} are:")
        for i,j in self.angajati.items():
            for k,l in j.items():
                if(l==departmentName):
                    print(k)

    def display_departments(self):
        print("The departments in the company are:")
        print(*(self.departamente.values()), sep = ",", end=" ")
        print()
