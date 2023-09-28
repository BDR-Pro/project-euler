def pali(num):
    palilist=str(num)
    palilist=list(palilist)
    for index , i in enumerate(palilist):
        if i!=palilist[len(palilist)-index-1]:
            return False
    return True

largest=0
final=1000
start=100
num=100
while num<final:
    for i in range(start,final):
        k=i*num
        #print(f"{i}*{num}={k}")
        if pali(k):
            if largest < k:
                largest=k
                print(f"pali = {i}*{num}={k}")

    num+=1