#dic สามารถสร้าง index เองได้ 
#dictionary -> key,value
#สามารถมี dict ย่อยได้
lis = ["green","yellow","red"]
tup = ("blue","pink","black")

animal = {"แมว":"cat","หมา":"dog"}#dict
print(animal)
animal.update({"ค้างคาว":"bat"})

for i in animal.keys():
    print(i)

for i in animal.values():
    print(i)

market={
    "ร้านป้าพร":{
        "name":"ป้าพร",
        "menu":["กะเพราไก่","ก๋วยเตี๋ยว"],
        "zone":'ตะวันออก'
    },
    "ร้านลุงป้อม":{
        "name":"น้าจ๊อบ",
        "menu":["มะม่วง","ทุเรียน"],
        "zone":'ทางเข้าตลาด'
    },
    "ร้านน้าใจ":{
        "name":"น้าใจ",
        "menu":["นมปั่น","ชาเย็น"],
        "zone":'ข้าง 7-11'
    }
}

print(market["ร้านป้าพร"]["menu"])

if "ทุเรียน" in market["ร้านป้าพร"]["menu"]:
    print("เป็น")
else :
    print("ไม่เป็น")