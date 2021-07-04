
n=int(input())  
list=[]

for i in range(n):
  addlist=[]
  for j in range(5):
    if j<2:
      addlist.append(input())
    else:
      addlist.append(int(input()))
  list.append(addlist)
a_sum=0
b_sum=0
c_sum=0

for i in range(n):
  a_sum+=list[i][2]
  b_sum+=list[i][3]
  c_sum+=list[i][4]
  
a_h=list[0][2]
b_h=list[0][3]
c_h=list[0][4]
a_k=0
b_k=0
c_k=0

for i in range(n):
  if list[i][2]>a_h: 
    a_h=list[i][2]
    a_k=i
  if list[i][3]>b_h: 
    b_h=list[i][3]
    b_k=i
  if list[i][4]>c_h: 
    c_h=list[i][4]
    c_k=i
    
print("KOR Average Score = %.2f"%(a_sum/n))
print("KOR Highest Score = %d"%(a_h))
print("Student Name: %s"%(list[a_k][0]))
print("Student Id: %s"%(list[a_k][1]))

print("ENG Average Score = %.2f"%(b_sum/n))
print("ENG Highest Score = %d"%(b_h))
print("Student Name: %s"%(list[b_k][0]))
print("Student Id: %s"%(list[b_k][1]))

print("MATH Average Score = %.2f"%(c_sum/n))
print("MATH Highest Score = %d"%(c_h))
print("Student Name: %s"%(list[c_k][0]))
print("Student Id: %s"%(list[c_k][1]))