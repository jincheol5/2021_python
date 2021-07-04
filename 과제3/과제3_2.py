n=int(input())

if n<2:
  print("Inavailable Number")
else:
  if n%2==0:
    n=2*n+1
  
  for i in range(n):
    for j in range(n):
      if i==0 or i==n-1 or i==int(n/2):
        print("*",end="")
      else:
        if j==0 or j==n-1 or j==int(n/2):
          print("*",end="")
        else:
          print(" ",end="")
    print()
    

