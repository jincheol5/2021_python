n=int(input())
m=int(input())
d=[]
for i in range(n):
  d2=[]
  for j in range(n):
    d2.append(0)
  d.append(d2)
s=[]
for i in range(m):
  s2=[]
  for j in range(m):
    s2.append(0)
  s.append(s2)


while(True):
  r=input()
  if r[0]=='d':
    k=r[3:]
    d[int(r[1])][int(r[2])]+=int(k)
    
  elif r[0]=='s':
    k=r[3:]
    s[int(r[1])][int(r[2])]+=int(k)
  

    
  elif r[0]=='n': break
  else: print("Wrong Input")

print(d)
print(s)