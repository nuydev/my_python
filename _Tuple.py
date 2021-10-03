#เก็บข้อมูลได้เหมือนlist แต่ tuple ไม่สามารถเปลี่ยนแปลงข้อมูลภายในได้

from typing import Tuple


tup = (1,2,"s")
lis = [1,2,"s"]

print(tup)
print(lis)
print(type(tup))
print(type(lis))

lis2 = list(tup)
print(lis2)
tup2 = tuple(lis)
print(tup2)
print(type(lis2))
print(type(tup2))