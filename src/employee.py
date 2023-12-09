"""
Employee
"""
# импорты должны происходить от корня, то есть надо импортировать src.services, а не просто services
from src.services import CURRENCIES, Salary
from datetime import datetime


class Date:

    def __set_name__(self, owner, name):
        print('Initing attribute')
        print(f'Owner is {owner}')
        print(f'Name is {name}')
        self._name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self._name]

    def __set__(self, instance, value):
        instance.__dict__[self._name] = datetime.strptime(value, '%Y:%m:%d')


class Employee:

    birth_date = Date()

    def __init__(self, name, surname, age, salary: Salary | None = None, birth_date='2020:12:13'):
        self.name = name
        self.surname = surname
        self._age = age
        self.__salary = salary #RUB
        self.birth_date = birth_date

    # декоратор не позволяет пользователю получать доступ к атрибуты и при этом пользователь им пользуется как атрибутом
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age: int):
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name.upper()

    def set_salary(self, amount, currency):
        self.__salary = Salary(amount=amount, currency=currency)

    def get_salary(self, currency):
        if self.__salary and (currency == self.__salary.currency):
            return self.__salary.amount
        return self.__count_salary(currency)

    def print_initials(self):
        print(f'Name: {self.name}, Surname: {self.surname}, Age: {self.age}')

    @staticmethod
    def say_hello(self):
        print('Hello!')

    def __count_salary(self, currency):
        match (currency, self.__salary.currency):
            case (CURRENCIES.RUBLE, CURRENCIES.DOLLAR): return self.__salary.amount * 88
            case (CURRENCIES.DOLLAR, CURRENCIES.RUBLE): return self.__salary.amount / 88
            case (CURRENCIES.RUBLE, CURRENCIES.EURO): return self.__salary.amount * 97
            case _: raise AttributeError # финальный кейс если все остальное не сработает


class Programmer(Employee):

    def count_salary(self):
        return 14000 * 5


class Manager(Employee):

    def count_salary(self):
        return 14000 * 2


class CEOManager(Manager):
    pass


class HRManager(Manager):
    pass


class FrontendEngineer(Programmer):
    pass


class BackendEngineer(Programmer):
    pass


class QAEngineer(Programmer):
    pass

if __name__ == '__main__': # информация о том, что мы вызвали этот файл из него же, а не импортировали
    # если сделать from employee import * тогда он не сможет инициализировать следующие переменные
    # поэтмоу лучше сделтаь просто перечисление того, что импортируешь
    pass