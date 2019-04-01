n=int(input())
o=n%10
O=n%100
if n==0 or o==0 or 5<=n<=9 or 5<=o<=9 or 11<=O<=19:
    print (n, 'программистов')
elif n==1 or o==1:
    print (n, 'программист')
elif 2<=n<=4 or 2<=o<=4:
    print (n, 'программиста')