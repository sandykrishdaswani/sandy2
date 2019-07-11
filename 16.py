sandy=int(input())
ss=list(map(int,input().split()[:sandy]))
count=0
for j in range(0,sandy+1):
   if(ss.count(j)==1):
      print(j)
