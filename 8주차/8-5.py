def countEvenNums(n):

  sum=0
  for i in range(1,n+1):
    if i%2==0:
      sum+=1
  return sum


n = int(input())
print("The number of evens is", countEvenNums(n))