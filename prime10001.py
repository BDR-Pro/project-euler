num=2
Primeiterator=0
def isprime(num):
    for i in range(2,num):
        if(num%i==0):
            return False
    return True
while True :
    if(isprime(num)):
        Primeiterator+=1
        print(num)
        if Primeiterator==10001:
            print(f"The 10001 Prime is {num}")
            break
    num+=1