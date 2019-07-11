sandy,t=map(int,input().split())
zoo=list(map(int,input().split()))
for j in range(0,t):
    zoo=[zoo[-1]]+zoo[:-1]
print(*zoo,end=' ')
