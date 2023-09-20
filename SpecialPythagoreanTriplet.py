import math
a,b,c = 0,0,0
check=False
for i in range(100000000):
    if(check):
        break
    a+=1
    b=0
    for i in range(10000000):
        b+=1
        c2=(a*a)+(b*b)
        c=math.sqrt(c2)
        print(f"a+b+c= {a+b+c}")
        print(f"a*b*c= {a*b*c}")
        if(a+b+c == 1000):
            print(int(a*b*c))
            check=True
            break
        if(a+b+c>1000):
            break
