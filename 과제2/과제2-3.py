n=input()
n1=n[0]+n[1]
n2=n[2]+n[3]
n3=n[4]+n[5]

if int(n1)<10:
  n0="20"
else:
  n0="19"

if int(n2)>12:
  print("Wrong")
elif int(n2)==0 or int(n3)==0:
  print("Wrong")
  
else:
  if int(n3)>31:
    print("Wrong")
    
  elif int(n2)==2 and int(n3)>29:
    print("Wrong")
    
  elif (int(n2)==4 or int(n2)==6 or int(n2)==9 or int(n2)==11 )and int(n3)>30:
    print("Wrong")
    
  else:
    sn=n0+n1
    
    if int(n2)<10:
      n2=n2[1]
    if int(n3)<10:
      n3=n3[1]
    print(sn+"/"+n2+"/"+n3)