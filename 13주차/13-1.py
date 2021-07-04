a={
  'white':1000,
  'blue':3000,
  'yellow':2000,
  'red':5000
}
sum=0
while(True):
  s=input()
  if s not in a:
    break
  else:
    sum+=a[s]

print("Total price =",sum)