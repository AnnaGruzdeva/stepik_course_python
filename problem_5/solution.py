a=int(input())
b=a%4
c=a%100
d=a%400
if b==0 and c!=0:
    print ('Високосный')
elif d==0:
    print ('Високосный')
else:
    print ('Обычный')