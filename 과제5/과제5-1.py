'''
딕셔너리 형태의 다음 정보가 있다.
family = {'father' : 'Lee', 'mother' : 'Seung', 'son' : 'Heon'}
딕셔너리를 추가 혹은 변경할 횟수 N을 입력받고, N개의 정보(key와 value)를 입력받는다.
그 후 숫자 M과 M개의 key를 입력받고 value값을 출력하는 프로그램을 작성하시오.
(단, key값에 맞는 value값이 없을 경우 none 출력)
'''
family = {'father' : 'Lee', 'mother' : 'Seung', 'son' : 'Heon'}
N=int(input())

for i in range(N):
  key=input()
  value=input()
  family[key]=value

a=[]

M=int(input())
for i in range(M):
  key=input()
  if key in family:
    a.append(family[key])
  else: a.append(None)
  
for b in a:
  if b==None: print("none")
  else: print(b)