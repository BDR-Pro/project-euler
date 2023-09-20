dvidable=0

for i in range(1,399999999):
    if dvidable==20:
        print(f"{i-1} is the number")
        break
    dvidable=0
    for k in range(1,21):          
        n=i%k
        if n !=0:
            break
        else:
            print(f"{i} is divisible by {k}")
            dvidable+=1
