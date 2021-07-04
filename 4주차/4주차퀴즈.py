s=""
while True:
    c=input()
    if c==';':
        break
    if c=='-':
        continue
    n=int(input())
    

    for i in range(n):
        s+=c
    
print("Result =",s)