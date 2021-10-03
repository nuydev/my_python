'''
1
12
123

'''
last = int(input("Enter Row :"))
for row in range(1,last+1):
    for column in range(1,row+1):
        print(column,end='')
    print(" ")

