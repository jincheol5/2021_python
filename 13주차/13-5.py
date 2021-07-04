Grade = [
['C', 'B', 'A', 'C', 'D'],
['F', 'D', 'C', 'D', 'B'],
['A', 'B', 'A', 'B', 'A'],
['A', 'A', 'B', 'C', 'D'],
['B', 'B', 'B', 'B', 'B'],
['B', 'B', 'C', 'D', 'F'],
['C', 'A', 'A', 'A', 'A'],
['D', 'A', 'A', 'C', 'F']
]
score={
  'A':4,
  'B':3,
  'C':2,
  'D':1,
  'F':0
}
subject=[3,3,3,2,1]
b=[]
for i in range(8):
  sum=0
  for j in range(5):
    sum+=score[Grade[i][j]]*subject[j]
  b.append(sum/12)

for i in range(8): print("%d %.2f"%(i+1,b[i]))