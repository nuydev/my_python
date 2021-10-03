'''
เมื่อต้องการเรียกใช้งานคุณสมบัติต่างๆในคลาสแม่ เช่น
Constructor,Method,Attribute

super().__init__(name)
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
    __departmentName = "บัญชี"
    def __init__(self,name,salary):
        #เรียกใช้Constructorและส่งparameter
        super().__init__(name,salary,self.__departmentName)

class Programmer(Employee):#สืบทอดคุณสมบัติ
    __departmentName = "พัฒนาระบบ"
    def __init__(self,name,salary):
        #เรียกใช้Constructorและส่งparameter
        super().__init__(name,salary,self.__departmentName)

class Sale(Employee):#สืบทอดคุณสมบัติ
    __departmentName = "ขายสินค้า"
    def __init__(self,name,salary):
        #เรียกใช้Constructorและส่งparameter
        super().__init__(name,salary,self.__departmentName)

acout = Accounting("may",25000)
prog = Programmer("Nuy",25000)

acout._showdata()
prog._showdata()
