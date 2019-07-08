sandy=list(input())
for i in range(0,len(dvi),2):
   sandy[i],sandy[i+1]=sandy[i+1],sandy[i]
uma=''.join(sandy)
print(uma)
