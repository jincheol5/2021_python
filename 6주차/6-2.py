n=int(input())

for i in range(n+1):
  for j in range(0,60):
    if i >= 10:
      if j >=10:
        print("%d:%d"%(i,j))
      else:
        print("%d:0%d"%(i,j))
    else:
      if j >=10:
        print("0%d:%d"%(i,j))
      else:
        print("0%d:0%d"%(i,j))