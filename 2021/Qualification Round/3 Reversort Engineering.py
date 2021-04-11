# https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d12d7#problem

T = int(input())
for t in range(T):
    N, C = map(int,input().split())
    if C < N-1 or N*(N+1)//2 <= C:
        print('Case #{}: IMPOSSIBLE'.format(t+1))
        continue
    
    C -= N-1
    chg = [1 for _ in range(N)]
    for x in range(N-1):
        if C == 0:
            break
        minim = min(N-x-1, C)
        chg[x] += minim
        C -= minim
    
    arr = [x+1 for x in range(N)]
    for x in range(N-1,-1,-1):
        for y in range(chg[x]//2):
            arr[x+y],arr[x+chg[x]-y-1] = arr[x+chg[x]-y-1],arr[x+y]
    
    ans = ' '.join(map(str,arr))
    print('Case #{}: {}'.format(t+1,ans))    