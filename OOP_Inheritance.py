'''
- สร้างสิ่งใหม่ขึ้นมาโดยสืบทอดคุณสมบัติมา
- ข้อดีคือ re-use ได้ นำสิ่งที่ดคยสร้างมาใช้ใหม่ได้
- ลูกได้คุณสมบัติจากคลาสแม่ยกว้น private attribute & private method
class Employee:
    pass
class Programer(Employee) =>class ลูก
'''
class Employee:
    _minSalary = 12000
    _maxSalary = 100000
    _companyName = "Cola"
    def __init__(self,name,salary,department):#private Method class Employee เท่านั้นที่สามารถเข้าถึงได้     
       # instance variable
        self.__name = name
        self.__salary = salary
        self._department = department

    def _showdata(self):#protected method
        print("Name = {}".format(self.__name))
        print("Salary = {}".format(self.__salary))
        print("Department = {}".format(self._department))

class Accounting(Employee):#สืบทอดคุณสมบัติ
    def __init__(self):
        pass

class Programmer(Employee):#สืบทอดคุณสมบัติ
    pass

class Sale(Employee):#สืบทอดคุณสมบัติ
    def __init__(self):
        pass

account = Accounting()
programmer = Programmer("Nuy",2500,"sony")#สืบทอดconstructorของแม่
sale = Sale()

print(account._maxSalary)
programmer._showdata()
print(sale._companyName)