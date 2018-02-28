from Employee import Employee


class Company:
    employee_register = []
    employee_count = 0

    def add_employee(self, empid, gender, age, sales, bmi, salary, birthday):
        emp = Employee(empid, gender, age, sales, bmi, salary, birthday)
        self.employee_register.append(emp)

    def get_all_employee(self):
        return self.employee_register

