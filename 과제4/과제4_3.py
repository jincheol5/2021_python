N1=int(input())
N2=int(input())

a=[]

#2중 리스트에 값 넣기 
for i in range(N1):
  b=[]
  for j in range(N2):
    
    b.append(int(input()))
  a.append(b) 


print(a)
print("%d X %d"%(N1,N2))

for i in range(N1):
  sum=0
  for j in range(N2):
    if j<(N2-2):
      sum+=a[i][j]
    
  a[i][N2-2]=sum
  a[i][N2-1]=sum/(N2-2)
  
print("before")
for i in range(N1):
  for j in range(N2):
    if j==(N2-1): print("%.1f"%a[i][j])
    else:print(a[i][j],end=" ")
  

print("after")

#평균값 기준으로 리스트 내림차순 정렬 
for j in range(N1):
  for i in range(N1-1):
    if a[i+1][N2-1]>a[i][N2-1]:
      s=a[i+1]
      a[i+1]=a[i]
      a[i]=s
    
for i in range(N1):
  for j in range(N2):
    if j==(N2-1): print("%.1f"%a[i][j])
    else:print(a[i][j],end=" ")
      
