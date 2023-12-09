import unittest
from src.employee import Employee
from src.services import Salary


class EmployeeBaseTests(unittest.TestCase):

    def test_create_employee_ideal(self):
        instance = Employee('1', '2', 20, salary=Salary(21000, 'rub'))
        self.assertEqual(instance.name, '1')
        self.assertEqual(instance.surname, '2')
        self.assertEqual(instance.age, 20)