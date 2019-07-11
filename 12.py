
san,tom=map(int,input().split())
ze=list(map(int,input().split()))
for j in range(0,t):
    ze=[ze[-1]]+ze[:-1]
print(*ze,end=' ')
