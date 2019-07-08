sa,ke=map(int,input().split())
sd=[]
for i in range(sa+1,ke+1):
    for x in range(2,i):
       if(i%x==0): 
           break
    else:
         sd.append(x)
print(len(sd)+1)
