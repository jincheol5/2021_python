score = [[90, 80, 100, 70, 80, 90, 100, 90], [60, 30, 90, 90, 85, 80, 75, 70], [85, 60, 99, 100, 90, 80, 70, 60]]
k=0
for i in score:
  
  min=i[0]
  for j in i:
    if j<min:
      min=j
  print("Min[%d] = %d"%(k,min))
  k+=1