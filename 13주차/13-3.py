a={
  'salmon roe':1000,
  'red sea bream':3000,
  'egg roll':1000,
  'shrimp':2000,
  'kimbab':1000,
  'tuna':5000
}

n=int(input())

sum=0
for i in range(n):
  s=input()
  if s in a:
    sum+=a[s]

print("Total price =",sum)