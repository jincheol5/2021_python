dic={}
n=int(input())
for i in range(n):
  name=input()
  if name in dic: dic[name]+=1
  else: dic[name]=1

print(dic)