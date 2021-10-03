#ซ่อนรายละเอียดการทำงาน
#ทำให้ภายนอกไม่สามารถเปลี่ยนแปลงข้อมูลภายในได้
#สร้างความปลอดภับให้ข้อมูล
#Access Modifier คือ ระดับการเข้าถึง class,Attribute,Method
'''
public => เข้าถึงได้ทั้วไป
protected(_) => classตัวเอง และclassลูก สามารถเข้าถึงได้
Private(__) => class ตัวเองใช้ได้เท่านั้น
'''
'''
class Employee:

    def __init__(self,name,salary):#private Method class Employee เท่านั้นที่สามารถเข้าถึงได้     
       #protected Attribute
        self._name = name
        self._salary = salary
        
    def _showdata(self):#protected Method
        print("Name = {}".format(self._name))
        print("Salary = {}".format(self._salary))

obj1 = Employee("Nuy",25000)
obj1._name = "NuyNuy" #เข้าถึงแบบ protected
obj1._showdata()
obj1.name = "Nuy" #รันผ่านแต่ attribute ไม่เปลี่ยน
print(obj1._name)
'''
class Employee:

    def __init__(self,name,salary):#private Method class Employee เท่านั้นที่สามารถเข้าถึงได้     
       #private Attribute
        self.__name = name
        self.__salary = salary
        #private Method
    def _showdata(self):#private method
        print("Name = {}".format(self.__name))
        print("Salary = {}".format(self.__salary))

obj1 = Employee("Nuy",25000)
obj1._showdata()
obj1.name = "Nuy" #รันผ่านแต่ attribute ไม่เปลี่ยน
obj1._name = "Nuy" #รันผ่านแต่ attribute ไม่เปลี่ยน
obj1._showdata()#ถ้าเป็น __showdata จะเรียกใช้ไม่ได้ จะใช้ได้ภายใน class Employee เท่านั้น