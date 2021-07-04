m=input()

f=open('python.txt','w')
f.write(m)
f.close()

n=int(input("n 입력 :"))
f=open('python.txt','r')
f.seek(n)
print(n," bytes 떨어진 위치에 있는 문자",f.read(1))
f.close()