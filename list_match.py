#โปรแกรมจับคู่สินค้าและราคา

order = ["นมปั่น","ชานม","ชาเขียว","กาแฟ"]
price = [29,19,19,25]

for x,y in zip(order,price):  #ใช้ zip จับคู่ list
    print("สินค้า ",x,"ราคา ",y)

for x,y in zip(order,price[::-1]):  #ใช้ zip จับคู่ list
    print("สินค้า ",x,"ราคา ",y)