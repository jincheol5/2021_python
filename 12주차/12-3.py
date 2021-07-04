a=[]

n=int(input())

for i in range(n):
  sum=0 
  a.append(input().split())
  
  for j in range(3):
    sum+=int(a[i][j])
  c=sum/3
  
  print("Student %d's Average Score :"%(i+1),round(c,2))
  









