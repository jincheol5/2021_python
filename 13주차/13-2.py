n=int(input())

a=[]

for i in range(n): 
  s=input().split(' ')
  a.append(s)  

sw=0
os=0
db=0

for i in range(n):
  for j in range(3):
    if j==0: sw+=int(a[i][j])
    elif j==1: os+=int(a[i][j])
    else: db+=int(a[i][j])
    
    
    
print("Average(SW) = %d"%(sw/n))
print("Average(OS) = %d"%(os/n))
print("Average(DB) = %d"%(db/n))