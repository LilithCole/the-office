from collections import defaultdict
from typing import Set

from employee import Employee


class TheOffice:

    def __init__(self, regional_manager: str, employees: Set[Employee], location: str):
        self.regional_manager = regional_manager
        self.employees = employees
        self.location = location
        self.sales = defaultdict(int)

    def __str__(self) -> str:
        return f"Welcome to The Office! The boss here is {self.regional_manager}."

    def record_sale(self, employee: Employee) -> None:
        """
        Method which records a sale made by an employee
        :param employee: The employee which made the sale
        :return: None
        """
        self.sales[employee] += 1

    def get_employee_sales(self, employee: Employee) -> int:
        """Method that returns the number of sales given an employee.
        :param employee: The employee whose sales number we are interested in
        :return: int: The total number of sales the employee as made
        """
        return self.sales[employee]

    def _fire_employee(self, employee: Employee) -> None:
        """
        Method which removes an employee from our database
        :param employee: The employee which we wish to remove
        :return: None
        """
        self.employees.remove(employee)
