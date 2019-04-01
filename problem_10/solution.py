a=int(input())
b=int(input())
c=int(input())
m=a
n=b
o=c
if b>=m>=c:
    m=b
    n=c
    o=a
elif b>=c>=m:
    m=b
    n=a
    o=c
elif c>=m>=b:
    m=c
    o=a
elif c>=b>=m:
    m=c
    n=a
    o=b
elif m>=b>=c:
    n=c
    o=b
print (m)
print (n)
print (o)