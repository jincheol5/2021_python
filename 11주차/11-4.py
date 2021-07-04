s=[]
sum=0
i=0
while(True):
  k=int(input())
  if k==0:
    break
  s.append(k)
  sum+=k
  i+=1
print(s)
print("Avg = %.2f"%(sum/i))