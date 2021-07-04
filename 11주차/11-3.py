s=[]
n =int(input())
sum=0
for i in range(n):
  k=int(input())
  s.append(k)
  sum+=k

print(s)
print("Avg = %.2f"%(sum/n))