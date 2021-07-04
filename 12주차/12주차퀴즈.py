user={}

while(True):
  n=int(input())
  if n==0: break
  elif n==1:
    name=input()
    score=int(input())
    user[name]=score
  else:
    name=input()
    if name in user: print("Name = %s, Score = %d"%(name,user[name]))
    else: print("No student")