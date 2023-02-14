from dataclasses import dataclass, field, asdict
from datetime import date
import unittest


@dataclass
class Employee:
    name: str
    age: int
    salary: float = field(default=0.0, repr=False, compare=False)
    hire_date: date = field(default_factory=date.today)

    def __post_init__(self):
        self.email = f'{self.name.lower().replace(" ", ".")}@example.com'

    def __str__(self):
        return f'Employee(name={self.name}, age={self.age}, email={self.email})'


class TestEmployee(unittest.TestCase):
    def test_default_values(self):
        employee = Employee('John Doe', 30)
        self.assertEqual(employee.name, 'John Doe')
        self.assertEqual(employee.age, 30)
        self.assertEqual(employee.salary, 0.0)
        self.assertEqual(employee.hire_date, date.today())
        self.assertEqual(employee.email, 'john.doe@example.com')

    def test_custom_values(self):
        hire_date = date(2022, 1, 1)
        employee = Employee('Jane Doe', 25, salary=50000.0, hire_date=hire_date)
        self.assertEqual(employee.name, 'Jane Doe')
        self.assertEqual(employee.age, 25)
        self.assertEqual(employee.salary, 50000.0)
        self.assertEqual(employee.hire_date, hire_date)
        self.assertEqual(employee.email, 'jane.doe@example.com')

    def test_asdict(self):
        hire_date = date(2022, 1, 1)
        employee = Employee('Jane Doe', 25, salary=50000.0, hire_date=hire_date)
        employee_data = asdict(employee)
        self.assertEqual(employee_data, {'name': 'Jane Doe', 'age': 25, 'salary': 50000.0, 'hire_date': hire_date})


if __name__ == '__main__':
    unittest.main()
