from Automation10_Projects.PythonAutomation.introduction_to_programming.curs_07.Exercitii_POO.company import company

employee1 = company('Bogdan', 'Mihalcea', '33', 'Engineer',1200)
employee1.add_department(0,'Hard Work Department')
employee1.add_department(1,'HR')
employee1.add_employee_to_department("3", "Marian Antonescu","HR")
employee1.add_employee_to_department("2", "Anton Popescu","Hard Work Department")
employee1.display_employees("Hard Work Department")