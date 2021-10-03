#เรียงลำดับชื่อ
student = ["ก้อง","วิว","ลิซ่า","จีซู","เจนนี่","แจส"]

print(student)
student.sort()#เรียงตัวอักษรก่อนค่อยเรียงสระ
print(student)
student.reverse()
print(student)

#เอาหลังมาหน้า
student = student[::-1]
print(student)