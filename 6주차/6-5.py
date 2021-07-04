n=int(input())
m=int(input())

for i in range(n):
  
  for j in range(n):
    if i==m-1:
      print("*",end="")
    else:
      if j==m-1:
        print("*",end="")
      else:
        print(" ",end="")
  print()