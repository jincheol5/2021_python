"""선택정렬"""
def ordered(s,a,b):
  for i in range(a,b):
    for j in range(i+1,b+1): 
      if s[i]<s[j]:
        s[i],s[j] = s[j],s[i] 
        print(s)
    
s=[]
N=int(input())
for i in range(N):
  a=int(input())
  s.append(a)

A=int(input())
B=int(input())

print(s)
ordered(s,A,B)
