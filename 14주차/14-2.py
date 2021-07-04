sum=0
f=open("p.txt",'r')

while True:
  line=f.readline()
  if not line: break
  sum+=int(line)
print("Total =",sum)

f.close()