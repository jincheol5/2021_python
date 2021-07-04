p=[]

n=int(input())

for i in range(n):
  for j in range(3):
    k=int(input())
    if i==0: p.append(k)
    else: 
      if k>p[j]: p[j]=k
  print(p)

s=0
max=p[s]

for i in range(3):
  if p[i]>max: 
    max=p[i]
    s=i 

if s==0: print("Person1 Win")
elif s==1: print("Person2 Win")
else: print("Person3 Win")

  
