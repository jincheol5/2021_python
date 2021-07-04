sum=0
for i in range(10):
  a=input()
  if a=="yellow":
    continue
  elif a=="red":
    break
  else:
    n=int(input())
    sum+=n

print("Sum =",sum)