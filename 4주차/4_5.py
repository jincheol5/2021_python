sum=0
count=0
while sum<20:
    n=int(input())
    count+=1
    if n!=4:
        sum+=n
    else:
        break

print("Count =",count)
print("Total =",sum)