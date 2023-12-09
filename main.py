"""
Startup for employee base
"""
from src.services import Salary, CURRENCIES
from src.employee import Employee, Programmer, Manager, \
    FrontendEngineer, BackendEngineer, QAEngineer, HRManager, CEOManager

# лучше делать импорт конкретных сущностей, а не всего вместе

if __name__ == '__main__':

    employee_1 = Programmer('FirstName', 'FirstSurname', 28)
    employee_1_1 = FrontendEngineer('FirstName', 'FirstSurname', 28)
    employee_1_2 = BackendEngineer('FirstName', 'FirstSurname', 28)
    employee_1_3 = QAEngineer('FirstName', 'FirstSurname', 28)

    employee_2 = Manager('SecondName', 'SecondSurname', 65)
    employee_2_1 = CEOManager('SecondName', 'SecondSurname', 65)
    employee_2_2 = HRManager('SecondName', 'SecondSurname', 65)

    employees = [employee_1, employee_1_1, employee_1_2, employee_1_3, employee_2, employee_2_1, employee_2_2]

    # employee_1.print_initials()  # Employee().print_initials(employee_1)
    # employee_2.print_initials()
    # print(employee_1.count_salary())
    # print(employee_2.count_salary())

    def print_employee_type(empl_obj):
        print(f'Does current employee belong to Employee type? {isinstance(empl_obj, Employee)}')
        print(f'Employee {empl_obj.name} is of {type(empl_obj)} type')
        print(f"Employee's salary is {empl_obj.count_salary()}")


    for employee in employees:
        print_employee_type(employee)

    salary_obj = Salary(amount=10000, currency=CURRENCIES.RUBLE)
    print(salary_obj)