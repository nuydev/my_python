'''
ตัวแปรที่ทำงานภายใน class ส่วนอื่น สามารถเข้าถึงข้อมูลส่วนนี้ได้เลย
(static attribute) โดยไม่จำเป็นต้องสร้าง object ขึ้นมา

'''
'''
คือตัวแปรที่อยู่ภายใน object สามารถเข้าถึงข้อมูลส่วนนี้โดยการสร้าง object ขึ้นมา
'''
class Employee:
    #class variable ต้องประกาศแบบ public,protected
    _minSalary = 12000
    _maxSalary = 100000
    def __init__(self,name,salary):#private Method class Employee เท่านั้นที่สามารถเข้าถึงได้     
       # instance variable
        self.__name = name
        self.__salary = salary

    def _showdata(self):#private method
        print("Name = {}".format(self.__name))
        print("Salary = {}".format(self.__salary))

obj1 = Employee("Nuy",25000)
obj1._showdata()

print(Employee._minSalary)#ไม่จำเป็นต้องสร้าง object ก้อเข้าถึงได้
print(Employee._maxSalary)