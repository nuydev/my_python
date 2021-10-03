#การสร้าง class & object
#ชื่อ ,  เงินเดือน
class Employee:
    #method
    def detail(self,name,salary):#self = this สามารถเอาค่าไปใช้ใน methode อื่นได้
        self.name = name
        self.salary = salary
    def showdata(self):
        print("Name = {}".format(self.name))
        print("Salary = {}".format(self.salary))



#การสร้างวัตถุ
obj1 = Employee()
obj1.detail("Nuy",25000)
obj1.showdata()

obj2 = Employee()
obj2.detail("May",50000)
obj2.showdata()