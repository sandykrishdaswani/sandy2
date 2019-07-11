anu=int(input())
ver=list(map(str,input()[:anu]))
vowels=['a','e','i','o','u','A','E','I','O','U']
rqr=[]
for i in ver:
   if i not in vowels:
      rqr.append(i)
print(''.join(map(str,rqr[::-1]))) 
