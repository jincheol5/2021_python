a=int(input())
sum=0
if a%10==1:
    a-=1
    sum+=1
a=a/10
if a%10==1:
    a-=1
    sum+=2
a=a/10
if a==1:
    sum+=4

print("decimal =",sum)
    