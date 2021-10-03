#เกมทายเลขลูกเต๋า 123456

import random

myrandom = random.randrange(1,7)#1-6
k = 1
while True:
    number = int(input("ป้อนคำตอบของคุณ = "))
    correct = (number==myrandom)
    if correct:
        print("ถูกต้อง!!")
        break
    if number<0 or k==3:
        print("ตอบผิดเหลือโอกาสอีก",3-k)
        print("เสียใจด้วย!")
        break
    print("ตอบผิดเหลือโอกาสอีก",3-k)
    k += 1
    