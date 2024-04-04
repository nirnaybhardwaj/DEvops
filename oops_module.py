import oops


emp1 = oops.Employee('Raju','raju@gmail.com','sales',50000)
emp2 = oops.Employee('Ankit','ankit@gmail.com','QA',5000)
# print(emp1.salary)
# print(emp2.gmail)

emp1.emp_info()
emp2.emp_info()

emp1.dept_change('Devops')
emp1.emp_info()

emp1.hello()
# print(oops.Employee.COMPANY)

