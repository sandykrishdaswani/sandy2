keer1,keer2=map(int,input().split())
for j in range(1,100000):
   if(j%keer1==0 and j%keer2==0):
      print(j)
      break
