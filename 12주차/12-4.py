user_info={
  'id':'software',
  'pw':'python'
}

key=input()
value=input()
id=0
v=0
if key != user_info['id']:
  id=1
  print("ID Mismatch!")
if value != user_info['pw']:
  v=1
  print("PW Mismatch!")

if id==0 and v==0:
  print("Success in Login")

