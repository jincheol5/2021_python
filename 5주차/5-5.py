n=int(input())

for i in range(n+1):
  if i>23:
    break
  else:
    if i>=10:
      print("%d : 00"%(i))
    else:
      print("0%d : 00"%(i))
  