a=[]

for i in range(5):
  b=int(input())
  a.append(b)

print("before =",end="")
print(a)

for i in range(5):
  for j in range(4):
    if a[j+1]<a[j]:
      t=a[j+1]
      a[j+1]=a[j]
      a[j]=t
print("after =",end="")
print(a)