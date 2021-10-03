#โปรแกรมหาค่า max,min

max,min = 0,0

while True:
    number = int(input("Enter Value :"))
    if number>max:
        max = number
    if number < min:
        min = number
    print("max = ",max,"min = ",min)