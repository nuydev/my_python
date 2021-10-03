#Destructor = methode สุดท้ายก่อนทำลาย Object เช่น คืนหน่วยความจำ
'''
def __del__(self):
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

    def __del__(self):
        print("Call Destructor")

obj1 = Employee("Nuy",25000)
obj1.showdata()
#สามารถเปลี่ยนค่าใน object ได้ เพราะยังไม่ถูกห่อหุ้ม
obj1.name = "May"
obj1.showdata()