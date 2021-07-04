n1=int(input())
n2=int(input())

for i in range(n1+1):
  for j in range(0,60):
    if i==n1 and j==n2+1:
      break
    if i<10:
      hour='0'+str(i)
    else:
      hour=str(i)
    if j<10:
      minute='0'+str(j)
    else:
      minute=str(j)
    print(hour+":"+minute)
    
  
    
  