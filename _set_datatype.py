#set เป็นกลุ่มของข้อมูลที่สมาชิกซ้ำกันไม่ได้ แต่ต่างชนิดกันได้ ลำดับไม่แน่นอน
#ไม่สามารถเข้าถึงแบบ index ได้
#สามารถใช้ union,difference,intersection ได้
fruit = {"มะม่วง","มะขาม","มะยม"}
print(fruit)
fruit.add("ส้ม")
fruit.add(1)
print(fruit)
fruit.update(["มะละกอ","กล้วย"])
print(fruit)
fruit.remove("ส้ม")
print(fruit)

for i in fruit:
    print("data :",i)

print(len(fruit))
print("กล้วย" in fruit)