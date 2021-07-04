user_info={
  'name':'David',
  'age':21,
  'address':'Gwangjin-gu, Seoul'

}

N=int(input())

for i in range(N):
  print("Edit #%d"%(i+1))
  key=input()
  if key=='age':
    value=int(input())
  else:
    value=input()
  user_info[key]=value

print("USER INFO")
for k,v in user_info.items():
  print(k,':',v)