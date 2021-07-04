s=[]

n=int(input())
for i in range(n):
  a=int(input())
  s.append(a)

index=int(input())
print(s[n-(index+1)])