n1=int(input())
n2=int(input())

for i in range(n1,n2+1):
  for j in range(1,10):
    print("%d X %d = %d"%(i,j,i*j))
    