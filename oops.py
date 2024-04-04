

class Employee:
    COMPANY = 'ABC.Pvt.ltd'
    # Constructor
    def __init__(self, name, gmail, dept, salary):
        self.name = name
        self.gmail = gmail
        self.dept = dept
        self.salary = salary

    def emp_info(self):
        print(f"Name is {self.name}")
        print(f"Gmail is {self.gmail}")
        print(f"Department is {self.dept}")
        print(f"Salary is {self.salary}")

    def dept_change(self, new_dept):
        self.dept = new_dept
        print(f"Department change to {new_dept}")

    # Decorator
    @staticmethod
    def hello():
        print('Hello')



