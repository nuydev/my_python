#Setter คือการกำหนดค่าให้ object
'''
def setName(self,newname):
    self.__name=newname #set ค่าให้ private attribute
'''
#Getter  คือการดึงค่าจาก object
'''
def getName(self):
    return self.__name #ดูค่า ใน private attribute
'''
class Employee:

    def __init__(self,name,salary):#private Method class Employee เท่านั้นที่สามารถเข้าถึงได้     
       #private Attribute
        self.__name = name
        self.__salary = salary

    def _showdata(self):#private method
        print("Name = {}".format(self.__name))
        print("Salary = {}".format(self.__salary))

    def setName(self,newname):
        self.__name=newname #set ค่าให้ private attribute

    def getName(self):
        return self.__name #ดูค่า ใน private attribute


obj1 = Employee("Nuy",25000)
obj1._showdata()
obj1.setName("NuyNuy")
obj1._showdata()
print(obj1.getName())