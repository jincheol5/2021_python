year=input()
startmonth=int(input())
lastmonth=int(input())
startday=int(input())
lastday=int(input())

if int(year)<10:
  year='0'+year
for i in range(startmonth,lastmonth+1):
  for j in range(startday,lastday+1):
    if i%2==0 and j>30:
      break

    if i<10:
      month='0'+str(i)
    else:
      month=str(i)
    if j<10:
      day='0'+str(j)
    else:
      day=str(j)

    if i==j:
      print(year+month+day+" Lucky Day!")
    else:
      print(year+month+day)
    
  
  
