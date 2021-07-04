n=int(input())

f=open('menu.txt','a')
for i in range(n):
  m_name=input("메뉴 이름 :")
  p=input("메뉴 가격 :")
  f.write(m_name+' '+p+'\n')
f.close

f=open('menu.txt','r')
print(f.read())
f.close()
