number=int(input())
sandy=0
aa=[]
bb=['a','a','b','i','k','l']
for i in range(0,number):
    aa.append(list(input()))
for i in aa:
    s=sorted(i)
    if(bb==s):
        sandy=sandy+1
print(sandy)
