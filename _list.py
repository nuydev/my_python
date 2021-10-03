#Primitive เก็บค่าได้แค่ 1 ค่า
#non Primitive เมื่อประกาศตัวแปรแล้วสามารถเก็บค่าได้มากกว่า 1

# list
number=[]# list ว่าง
number=[1,2,3,4,5,5]
name=["a","b","c"]
all=[10,"a",True,3.14,-10]
#นิยามแบบ constructer
name2=list(["a2","b2","c2"])
print(number)
print(name)
print(name2)
print(all)
print(type(name))
print(type(name2))
print(all[2]) #True
print(all[-3])#True
print(all[:3])
print(all[1:3])
print("ความยาวnumber",len(number))
print("ความยาวall",len(all))
#การแก้ไข Var[index]=value
#ต่อท้ายlist จะใช้ var.append()
#insert ระบุตำแหน่ง
#remove ระบุข้อมูลที่จะลบ
#popเอาตัวสุดท้ายออก
#copy list ได้
#list+listได้
#count นับจำนวนขอมูลในlistตามที่กำหนด
#extend เพิ่มข้อมูลจากlistอื่นได้
if 10 in number:
    print("yes")
else :
    print("No")

for x in name:
    print(x,end=" ")
print("")
print("")
for y in all:
    print(y)
print("")
for z in range(len(name)):
    print(name[z])