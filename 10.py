ps=input()
ps=ps.split()
san=ps[0]
s=ps[1]
count=0
i=0
while(i<len(san) and count<2):
    if(san[i]!=s[i]):
        count+=1
    i+=1
if(count==1 or count==0):
    print("yes")
else:
    print("no")
