s=[]
n=int(input())
for i in range(n):
  a=int(input())
  s.append(a)

while(True):
  a=int(input())
  if a==0: break
  if a in s: print("YES")
  else : print("NO")