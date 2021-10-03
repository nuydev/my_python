'''
คือฟังก์ชันที่ทำงานกับ class และ object
isinstance => เช็คว่า object นี้ถูกสร้างจาก class ที่เรานิยามหรือไม่
dir => แสดง Attribute และ Method
__class__ => แสดงชื่อ class ของ object

'''
class Employee:

    def __init__(self,name,salary):  
        print("Default Constructor")      
        self.name = name
        self.salary = salary

    def showdata(self):
        print("Name = {}".format(self.name))
        print("Salary = {}".format(self.salary))

obj1 = Employee("Nuy",25000)
obj1.showdata()

print(isinstance(obj1,Employee))
print(dir(obj1))
print(obj1.__class__)