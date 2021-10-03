# BMI = น้ำหนัก (kg) / ส่วนสูง * ส่วนสูง (m)

#input / convert to interger
weight = int(input("ป้อนน้ำหนักของคุณ (kg) :"))
high = int(input("ป้อนส่วนสูงของคุณ (cm) :"))

#process
high = high/100
bmi = weight/(high*high)

#output
print("BMI = %.2f" %(bmi))
