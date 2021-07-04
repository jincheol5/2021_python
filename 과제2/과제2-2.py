age=int(input())
km=int(input())

if age<14:
  rates=450
  if km>10:
    km-=10
    k=int(km/5)
    if k<1:
      rates+=100
    else:
      if km%5!=0:
        k+=1
      rates+=100*k

  print("Child rates : %d won"%(rates))
elif age<19:
  rates=720
  if km>10:
    km-=10
    k=int(km/5)
    if k<1:
      rates+=100
    else:
      if km%5!=0:
        k+=1
      rates+=100*k
  print("Youth rates : %d won"%(rates))
else:
  rates=1250
  if km>10:
    km-=10
    k=int(km/5)
    if k<1:
      rates+=100
    else:
      if km%5!=0:
        k+=1
      rates+=100*k
      
  print("Regular rates : %d won"%(rates))