a=[2,3,1,4]
max=a[0]
print("a =",a)
for i in range(4):
  for j in range(i+1):
    if a[j]>max:
      max=a[j]
  print("%d %d"%(i,max))


print("Max = %d"%max)    
    