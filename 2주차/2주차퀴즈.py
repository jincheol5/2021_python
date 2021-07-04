second=int(input())
day=0
hour=0
min=0
if second >= 86400:
    day=(int)(second/86400)
    second=second%86400

if second >=3600:
    hour=(int)(second/3600)
    second=second%3600

if second >=60:
    min=(int)(second/60)
    second=second%60

    
print("%d days %.2d:%.2d:%.2d"%(day,hour,min,second))
