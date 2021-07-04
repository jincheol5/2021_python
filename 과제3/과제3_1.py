a=["scissors","rock","paper"]

win=0
draw=0
lose=0
c=0

for i in range(10):
  opp=int(input())
  me=int(input())
  print("Opponent : %s"%(a[opp]))
  print("Me : %s"%(a[me]))
  c+=1
  if opp==0 and me==1: win+=1
  elif opp==0 and me==2: lose+=1
  elif opp==0 and me ==0: draw+=1
  elif opp==1 and me==2: win+=1
  elif opp==1 and me==0: lose+=1
  elif opp==1 and me ==1: draw+=1
  elif opp==2 and me==0: win+=1
  elif opp==2 and me==1: lose+=1
  else: draw+=1
  
  if win == 3: break
  
print("Win : %d, Draw : %d, Lose : %d"%(win,draw,lose))
print("Odds : %.2f%%"%((win/c)*100))