h=int(input())
min=int(input())
M=int(input())
N=int(input())

starthm=60*h+min
count=0
for i in range(starthm,22*60+1,M):
  if count>=N:
    break
  hour=i/60
  minute=i%60
  if hour>=10:
    if minute>=10:
      print("%d:%d Carrot Time!"%(hour,minute))
    else:
      print("%d:0%d Carrot Time!"%(hour,minute))
  else:
    if minute>=10:
      print("0%d:%d Carrot Time!"%(hour,minute))
    else:
      print("0%d:0%d Carrot Time!"%(hour,minute))
  count+=1

if count!=N:
  print("Emergency!")