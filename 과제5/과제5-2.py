'''
n명의 학생의 이름과 3회의 모의고사 점수를 입력을 받는다.
이 때, 학생의 이름을 key로 3회의 모의고사 점수 평균을 value로 사용하여 딕셔너리 배열을 만들어,
stop이 입력되기 전까지 평균 점수에 대한 학생의 등수를 출력하는 프로그램을 작성하시오.
만약 딕셔너리에 존재하지 않는 이름을 검색한다면 does not exist!를 출력하도록 한다.
(단, 평균 점수 계산 시 소수점 둘째짜리에서 반올림하며, 평균 점수가 같은 경우는 없다)
'''

d={}
n=int(input())
sc=[]
for i in range(n):
  name=input()
  s=input().split(" ")
  sum=0
  for j in range(len(s)):
    sum+=int(s[j])
  score=sum/3
  d[name]=round(score,2)
  sc.append(round(score,2))

#오름차순 정렬 후 내림차순으로 변경
sc.sort()
sc.reverse()



while True:
  s=input()
  if s=='stop': break
  if s in d:
    count=0
    for i in sc:
      count+=1
      if d[s]==i: print(count)
  else: print('does not exist!')
  
      


  
