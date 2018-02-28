class Data_parser:

    filename = 'Data.txt'
    myemp=[]


def __init__(self,empid,gender,age,sales,bmi,salary,birthday):
    self.empid = empid
    self.gender =gender
    self.age= age
    self.sales= sales
    self.bmi =bmi
    self.salary = salary
    self.birthday=birthday


def open_file(filename):
    global myemp
    with open(filename) as f:
        data = f.readlines()
        print(data)
        for x in data:
            myemp.append(x)
            print(myemp)
            group = lambda t, n: zip(*[t[i::n]for i in range(n)])
            group([myemp],6)

