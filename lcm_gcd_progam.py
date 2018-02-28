a=int(input("enter 1st num:"))
b=int(input("enter 2nd num:"))
s=a
d=b
while(b!=0):
    r=a%b
    a=b
    b=r
print("gcd",a)
l=s*d/a
print("lcm",l)

