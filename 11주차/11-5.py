s=[0,1,2,3,4,5,6,7,8,9]

idx=int(input())
n=int(input())
print(s)
for i in range(len(s)):
  if i==idx:
    s[i]=n
    
print(s)