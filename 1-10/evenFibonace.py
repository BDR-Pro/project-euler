fib=[1,2]
i,j=0,1
while True:
    num=0
    num+=(fib[i]+fib[j])
    if num>4000000: break
    fib.append(num)
    i=j
    j+=1

print(fib)
num=0
for i in fib:
    if i%2==0:
        num+=i
print(num)
