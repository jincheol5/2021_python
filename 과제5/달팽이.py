def twolist(li,N):
  
  for i in range(N):
    a=[]
    for j in range(N):
      a.append(0)
    
    li.append(a)
    
  return li
def show(li,N):
  for i in range(N):
    for j in range(N):
      print("%03d"%(li[i][j]),end=" ")
    print()

#90도씩 반시계방향으로 회전시켜주는 함수 
def spin(li,a,N):
  a=twolist(a,N)
  for i in range(N):
    for j in range(N):
      a[N-1-j][i]=li[i][j]
      
  return a


li=[]
N=int(input())

li=twolist(li,N)

row=0
col=-1
change=1
value=1
n=N

while n>0:
  for i in range(n):
    col+=change
    li[row][col]=value
    value+=1
    
  n-=1
  if(n==0): break
  
  for i in range(n):
    row+=change
    li[row][col]=value
    value+=1 
  change*=-1 
  
show(li,N)

print("")
#90 
c=[]
c=spin(li,c,N)


show(c,N)

print("")

d=[]
d=spin(c,d,N)
show(d,N)