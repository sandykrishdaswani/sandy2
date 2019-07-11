sandy11=int(input())
for j in range(2,sandy11+1):
  if(sandy11%j==0):
      sandy2=0
      for m in range(2,j+1):
          if(j%m==0) and (m!=j):
              sandy2=1
              break
      if(sandy2==0):
          print(j,end=' ')
       
