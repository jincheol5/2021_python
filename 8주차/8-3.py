
def sum_digit(n):
  sum=0
  while(n>=10):
    sum+=n%10
    n=int(n/10)
  sum+=int(n)

  return sum
n = int(input())
result = sum_digit(n)
print(result)