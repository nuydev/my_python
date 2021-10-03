#comment 1 line
'''
comment
comment 
comment
'''
print("Hello World 12345")
print('Hello2')
print('''Hello3''')
# เราสามารถใช้ ' " '''ก็ได้

print(-1)
print(0)
print(1)
print(3.99)
print(True)
print(False)

name = 'Teerawat'# กำหนดค่า string มาเก็บไว้ในตัวแปร name
print('My name is ', name)# แทนค่า name เข้าไปในค่าทีต้องการ print
print('My name is '+   name)
age = 23
print('I am %d years old' %(age)) # %d = decimal โดยดึงค่ามาจาก age
grade = 3.34
print('my grade is %.2f' %(grade))# .2f = กำหนดทศนิยม 2 ตำแหน่ง
print('My name is %s, I\'m %d years old' %(name,age))
# เอามายำรวมกัน ระหว่าง string and decimal ส่วน \ ใช้เพื่อให้โปรแกรมมันข้าม single quote หลัง I ไปเลย (ignore ตัวถัดไป)
print("My name is %s, I'm %d years old" %(name,age))
print("Teerawat \t"+"Homthong\n")
print(age,end=' ')#ถ้าไม่ใส่ end จะ print แบบขึ้นบรรทัดใหม่
print(grade)
ss = 5222
print("salary = {}".format(ss))