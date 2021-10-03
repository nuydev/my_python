
name = "   teerawat   "

print(name[0])
print(name[5])
print(name[:5])
print(name[5:])
print(name[1:4])
print(name[-1])
print(name[-2])
print(name[-2:])
print(len(name))
name = name.strip()#ลบช่องว่างString : :ซ้ายใช้ lstrip , ขวา rstrip
print(len(name))
print(name.upper())
print(name.lower())
print(name.capitalize()) #ตัวแรกพิมพ์ใหม่
name = name.replace("t","n",1) 
print(name)

#เช็คว่ามีในString
x = "t" in name
print(x)
