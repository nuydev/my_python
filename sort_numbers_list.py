#โปรแกรมเรียงตัวเลข
number = [] #listว่าง
odd=[]#เก็บเลขคี่
even=[]#เก็บเลขคู่
while True:
    x = int(input("Enter Number: "))
    if x<0:
        break
    number.append(x) #เก็บข้อมูลตัวเลขเข้าlist number
    if x%2 == 0:
        even.append(x)
    else :
        odd.append(x)

print("before :",number)
number.sort()
print("min>max :",number)
number.reverse()
print("max>min :",number)
print("min = ",min(number))
print("max = ",max(number))
print("sum = ",sum(number))
print("เลขคี่ = ",odd)
print("เลขคู่ = ",even)
print("จบโปรแกรม")