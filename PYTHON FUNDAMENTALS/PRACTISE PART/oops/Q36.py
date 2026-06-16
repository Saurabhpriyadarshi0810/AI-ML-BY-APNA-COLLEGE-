from abc import ABC , abstractmethod

class employee :
    @abstractmethod
    def calculate_salary(self):
        pass

class intern(employee):
    salary = 0 

    def __init__(self, salary):
        self.salary = salary

    def calculate_salary(self):
        print(f"Salary of a intern is {self.salary}")


class contract_employee(employee):
    salary = 0 

    def __init__(self, salary):
        self.salary = salary

    def calculate_salary(self):
        print(f"Salary of a intern contract employee  is {self.salary}")

class full_time_employee(employee):
    salary = 0 

    def __init__(self, salary):
        self.salary = salary

    def calculate_salary(self):
        print(f"Salary of a full time employee is {self.salary}")


i = intern(10000)
i.calculate_salary()

c = contract_employee(20000)
c.calculate_salary()

f = full_time_employee(30000)
f.calculate_salary()
