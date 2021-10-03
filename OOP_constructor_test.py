#Constructor = methode ที่ทำงานทันทีหลังจากสร้าง Object
'''
def __init__(self):
    pass
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
#สามารถเปลี่ยนค่าใน object ได้ เพราะยังไม่ถูกห่อหุ้ม
obj1.name = "May"
obj1.showdata()


