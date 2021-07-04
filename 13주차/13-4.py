a=[]
for i in range(8):
  a.append(int(input()))

s=a[0]
for i in range(8):
  for j in range(7):
    if a[j+1]>a[j]:
      k=a[j+1]
      a[j+1]=a[j]
      a[j]=k

for i in range(8): print(a[i])