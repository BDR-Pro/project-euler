def isnotprime(num):
    for i in range(2,num):
        if(num%i==0):
            return False
    return True

for i in range(1,600851475143):
    if 600851475143%i==0:
        if isnotprime(i):
            print(i)
