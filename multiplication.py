#โปรแกรมสูตรคูณ
start1 = int(input("ป้อนแม่สูตรคูณ :"))
start2 = int(input("ป้อนแม่สูตรคูณ :"))

for x in range(start1,start2):
    print("แม่ = ",x)
    for y in range(1,13):
        print(x,"x",y," = ",(x*y))