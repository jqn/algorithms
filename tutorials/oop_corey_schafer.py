"""
Corey Schafer Python OOP tutorials
----------------------------------

Corey Schafer Python Object-Oriented Programming tutorials YouTube playlist:
https://www.youtube.com/playlist?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc

Completed code
"""
import datetime


class Employee:
    """Baseclass constructor for employee data.
    ---
    """

    # Create class variables
    raise_amount = 0.04
    total_emps = 0

    def __init__(self, first, last, pay):
        """Sets employee attributes."""
        self.first = first
        self.last = last
        self.pay = int(pay)
        Employee.total_emps += 1

    def __repr__(self):
        return f"Employee('{self.first}', '{self.last}', {self.pay})"

    def __str__(self):
        return f"{self.fullname} - {self.email}"

    def apply_raise(self):
        """Calculates the new salary after a pay raise."""
        self.pay = int(self.pay * (1 + self.raise_amount))
        return self.pay

    @property
    def email(self):
        return f"{self.first}.{self.last}@email.com"

    @property
    def fullname(self):
        """Constructs employee full name."""
        return f"{self.first} {self.last}"

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last
        print(f"Full name set to {name} with setter method.")

    @fullname.deleter
    def fullname(self):
        print(f"Delete name {self.fullname}!")
        self.first = None
        self.last = None

    @classmethod
    def set_raise_amount(cls, amount):
        """Set the amount of the pay raise."""
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        """Parse employee data out of a string."""
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

    @staticmethod
    def weekday(day):
        """Determine if a given date is a weekday."""
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


class Developer(Employee):
    """Class constructor for developers that inherits the Employee class."""

    raise_amount = 0.10

    def __init__(self, first, last, pay, lang):
        """Set employee attributes for the Developer subclass."""
        super().__init__(first, last, pay)
        self.lang = lang

    @classmethod
    def from_string(cls, emp_str):
        """Parse developer data out of a string."""
        # TODO: Can I inherit the Employee.from_string classmethod?
        first, last, pay, lang = emp_str.split("-")
        return cls(first, last, pay, lang)


class Manager(Employee):
    """Class constructor for managers that inherits the Employee class."""

    def __init__(self, first, last, pay, employees=None):
        """Set employee attributes for the Manager subclass."""
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        """Add an employee to the manager's employees list."""
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        """Remove an employee from the manager's employees list."""
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        """Print the list of the manager's employees."""
        print(f"People managed by {self.fullname}:")
        for emp in self.employees:
            print(f"-> {emp.fullname}")


def class_example():
    """Instantiate the classes from the module with example information.
    ---
    """
    dev_1 = Developer("Corey", "Schafer", 50000, "Python")
    dev_1.fullname = "Corey SchaferSetter"
    dev_2 = Developer("Test", "User", 60000, "Java")
    dev_3 = Developer.from_string("Jane-Doe-90000-Scala")
    # dev_3 = Developer("Jane", "Doe", 90000, "Scala")
    devs = [dev_1, dev_2, dev_3]
    emp_1 = Employee("Employee", "One", 50000)
    emp_2 = Employee("Employee", "Two", 60000)
    emp_3 = Employee.from_string("John-Doe-70000")
    emps = [emp_1, emp_2, emp_3]
    mgr_1 = Manager("Sue", "Smith", 120000, [dev_1])
    # Print desired output
    print(f"Total people: {Employee.total_emps}")
    for dev in devs:
        print(f"Developer {dev.fullname} email: {dev.email}")
        print(f"Programming language of choice: {dev.lang}")
        print(
            f"Raise for {dev.fullname}: {dev.raise_amount:.0%}.",
            f"Salary: {dev.pay} -> {dev.apply_raise()}",
        )
    for emp in emps:
        emp.apply_raise()
        print(f"Employee {emp.fullname} email: {emp.email}")
        print(
            f"Raise for {emp.fullname}: {emp.raise_amount:.0%}.",
            f"Salary: {emp.pay} -> {emp.apply_raise()}",
        )
    mgr_1.add_emp(dev_2)
    mgr_1.print_emps()
    del emp_1.fullname
    print(f"New emp_1 name: {emp_1.fullname}")
    tut_date = datetime.date(2018, 11, 9)
    print(f"Did I do this tutorial on a weekday? {Employee.weekday(tut_date)}")
    # Print information on the developer class
    # print(help(Developer))


if __name__ == "__main__":
    class_example()
