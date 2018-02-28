from Company import Company
from View import View
import re
company = Company()
company.add_employee("EMP001", "M", 23, 201, "Normal", 20000, "01/08/1991")


def get_employees():
    the_list = company.get_all_employee()
    for x in the_list:
        info = x.get_all_data()
        for i in info:
            View.display(i)


def add_employee():
    id = View.input("Enter Employee ID ")
    gender = View.input("Enter Employee gender ")
    age = int(View.input("Enter Employee age "))
    sales = int(View.input("Enter Employee sales "))
    bmi = View.input("Enter Employee bmi ")
    salary = int(View.input("Enter Employee salary "))
    birthday = View.input("Enter Employee Bday ")
    company.add_employee(id, gender, age, sales, bmi, salary, birthday)



get_employees()
add_employee()
get_employees()


