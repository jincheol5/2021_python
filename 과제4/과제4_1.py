a=[]

while(True):
  
  if len(a)>=10:
    print(a) 
    break
  n=int(input())
  if n>0: a.append(n)
  else:
    n=n*(-1)
    if n>len(a):
      print("error") 
      break
    else:
      for i in range(len(a)-1,len(a)-1-n,-1):
        del a[i]  
  
  