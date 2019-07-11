lod=int(input())
log=0
while(lod>0):
    p=lod%10
    lod=int(lod/10)
    log+=p*p
print(log)  
