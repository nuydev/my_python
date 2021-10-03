'''
if expression:
    Statement

'''
age = int(input("Enter Age : "))

if age>=15:
    print("Hello Mr.")

else :
    print("Hello Babe!")
    print("555")

print("จบโปรแกรม")

# ถ้าต้องการให้เป็นจริงแค่ case เดียว ให้ใช้ elif
'''
if expression:
    Statement
elif expression:
    Statement
else :
    Statement

'''

#Ternary Operator เงื่อนไขบรรทัดเดียว
print("วัยรุ่น") if age>=15 else print("วัยเด็ก")
'''

'''
if age>=15:
    if age==15:
        print("ม.3")
    else :
        pass

