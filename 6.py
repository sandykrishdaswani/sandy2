san,uma=map(str,input().split())
if(len(s)!=len(u)):
    print("no")
else :
    s1=[san.count(i) for i in san]
    s2=[uma.count(i) for i in uma]
if(s1==s2):
    print("yes")
else:
    print("no")
