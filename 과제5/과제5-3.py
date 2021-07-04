'''
달팽이 배열 회전시키기 문제
각 회전마다 규칙 찾으면 된다 
n , n-1 , n-1 , n-2 , n-2 , n-3 ...식으로 
'''
#2차원 배열 0으로 초기화 후 리턴 
def make2list(li,n):
  for i in range(n):
    p=[]
    for j in range(n):
      p.append(0)
    li.append(p)
  return li


N=int(input())

#2차원 배열 0으로 초기화 
a=[]
a=make2list(a,N)

#달팽이 배열 생성 
value=1
row=0
col=-1
change=1
n=N
while n>0:
  for i in range(n):
    col+=change
    a[row][col]=value 
    value+=1
  n-=1
  if(n==0): break
  for i in range(n):
    row+=change
    a[row][col]=value
    value+=1
  change*=-1
  

print("#0")
for i in range(N):
  for j in range(N):
    print("%03d "%(a[i][j]),end="")
  print()
    
print("#90")
c=[]
c=make2list(c,N)
for i in range(N):
  for j in range(N):
    c[j][N-1-i]=a[i][j]
    
for i in c:
  for j in i:
    print("%03d "%(j),end="")
  print()
  
print("#180")
c=[]
c=make2list(c,N)
for i in range(N):
  for j in range(N):
    c[N-1-i][N-1-j]=a[i][j]
    
for i in c:
  for j in i:
    print("%03d "%(j),end="")
  print()
    
  

print("#270")
c=[]
c=make2list(c,N)
for i in range(N):
  for j in range(N):
    c[N-1-j][i]=a[i][j]
    
for i in c:
  for j in i:
    print("%03d "%(j),end="")
  print()
  
print("#360")
for i in range(N):
  for j in range(N):
    print("%03d "%(a[i][j]),end="")
  print()