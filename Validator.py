import re
from View import View


class Validator:

    def validate_empid(empid):
        validating_empid = re.match(r"^[A-Z][0-9]{3}", empid)
        if validating_empid:
            print("Valid Data")
            return
        else:
            print("Invalid data")
            return


    def validate_gender(gender):
        gender_values=['M','F']
        for x in gender_values:
             if gender == x:
                print("Valid Data")
                return
             else:
                print("Invalid data")
                return


    def validate_bmi(bmi):
        bmi_values=['Normal','Overweight','Obesity','Underweight']
        for x in bmi_values:
             if bmi == x:
                print("Valid Data")
                return
             else:
                print("Invalid data")
                return


    def validate_sales(sales):

        validating_value = re.match(r"^[0-9]{3}",sales)
        if validating_value:
         print("Valid Data")
         return
        else:
         print("Invalid data")
         return


    def validate_salary(salary):

        validating_sal = re.match(r"^[0-9]{2,3}",salary)
        if validating_sal:
         print("Valid Data")
         return
        else:
         print("Invalid data")
         return

    validate_empid(View.input("Enter Employee ID "))
    validate_gender(View.input("Enter Employee gender "))
    validate_sales(sales=View.input("Enter Employee sales "))
    validate_bmi(bmi=View.input("Enter Employee bmi "))
    validate_salary(salary=View.input("Enter Employee salary "))