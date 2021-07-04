def judyear(year): #윤년 판단 함수 
  jud=0 #1이면 윤년 

  if year%4==0:
    if year%100==0:
      if year%400==0:
        jud=1
    else:
      jud=1
  return jud

def returnday(year,month,day): #해당 일에서 다음 달 1일 까지의 차이 반환 
  allday =0
  if month==4 or month==6 or month==9 or month==11:
    allday+=(30-day)
  elif month==2:
    if judyear(year)==1:
      allday+=(29-day)
    else:
      allday+=(28-day)
  else:
    allday+=(31-day)
    
  return allday+1


  
    



year = int(input())
month = int(input())
day = int(input())

period=0
while(True):
  if year==2021 and month==5:
    break
  period+=returnday(year, month, day)
  if month==12:
    year+=1
    month=1
  else:
    month+=1
    day=1
  
period+=3 # 1일 부터 4일 까지의 차이 

print(period)

    
