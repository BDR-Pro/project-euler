import time

def numdivisors(triangle):
  factors = 0
  for i in range(1, int((triangle ** 0.5)) + 1):
    if triangle % i == 0:
      factors += 1
  return factors * 2



tri=[1,3,6]
numdvisor=0
start=time.time()
while numdvisor<500:
    index=len(tri)
    x=0
    x=tri[-1]+index+1
    tri.append(x)
    numdvisor=numdivisors(x)-1

print(f"number of dvisor : {numdvisor}")
print(f"last elemnt: {tri[-1]}")
#print(f"the triangle list is {tri}")
end=time.time()
timems=end-start
print(f"it takes:  {timems}")