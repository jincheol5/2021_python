s=[8,6,9,10,4,7,10,6,8,7]

max=s[0]
k=0
for i in range(len(s)):
  if s[i]>max:
    k=i
    max=s[i]

print("s =",s)
print("Max =",max)
print("Idx =",k)