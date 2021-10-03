data={"191":"แจ้งเหตุด่วน","1668":"รถโรงพยาบาล","1447":"ดับเพลิง"}

def searchNumber(message):
    for key , value in data.items():
        if value==message:
            print("เบอร์ติดต่อ = ",key)
            break
        else :
            print("ไม่มีข้อมูล")
            return

searchNumber("แจ้งเหตุด่วน")