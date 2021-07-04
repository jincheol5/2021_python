
def process(n):
  k=0
  for i in range(1,n+1):
    if n%i==0:
      k+=1
      if i!=1:
        s=i
  if s==n and k==2:
    print("%d is prime number"%(s))
  else:
    print("The number of factors of %d is %d"%(n,k))


n = int(input())
process(n)