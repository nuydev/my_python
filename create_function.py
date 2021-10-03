#การสร้าง function
# def name ():
#    statement

def sayhi():
    print("Hello function")

sayhi()

# Arguments / Parameter

def addition(a,b):
    print("ผลรวม = ",a+b)

x=5
y=9
addition(x,y)

# *agrs ใส่หลายค่าพร้อมกัน

def add(*number):
    print(number)
    print(type(number))
    sum=0
    for i in range(len(number)):
        sum+=number[i]
    print(sum)

add(10,5)
add(10,5,6)

def displayFruit(item):
     for i in range(len(item)):
         print("ผลไม้ชิ้นที่ ",i+1 ," = " , item[i])

def displayVet(item):
    for i in range(len(item)):
         print("ผักชนิดที่ ",i+1 ," = " , item[i])

fruit=["มะม่วง","มะละกอ","ฝรั่ง","มะนาว"]
vet=('ชะอม','ผักกาด','คะน้า')

displayFruit(vet)
displayVet(vet)

# function return ค่า

def randomNumber(x):
    if len(x)<3 :
        return
        
    if x == "100":
        print("ถูกหวย")
        return 1000
    else :
        print("ไม่ถูกหวย")
        return 0


money=randomNumber("100")
print("เงินรางวัล = ",money)