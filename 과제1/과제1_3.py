N=int(input())
name=input()
age=int(input())
phone=int(input())
s=""
for i in range(N):
    s+=name
print("Name :",s)

    
y=2021-(age-1)
passwordage=y/N
print("Age :",(int)(passwordage))
print("Number :",phone*N)
