num=int(input())
s1=0
s2=0
for i in range(1,num+1):
  if i%2==0:
    s2+=i
  else:
    s1+=i

print("Sum1 =",s1)
print("Sum2 =",s2)