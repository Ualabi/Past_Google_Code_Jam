import sys 
sys.setrecursionlimit(10**6) 

def solve(n,k,s,c):
    if c == abs(n)+abs(k):
        return c
    if s == '':
        return 'IMPOSSIBLE'
    if s[0] == 'N':    k += 1
    elif s[0] == 'S':  k -= 1
    elif s[0] == 'W':  n -= 1
    elif s[0] == 'E':  n += 1
    
    if c == abs(n)+abs(k):
        return c+1
    else:
        return solve(n,k,s[1:],c+1)
        
T = int(input())
for i in range(T):
    n, k, s = input().split()
    n = int(n)
    k = int(k)
    ans = solve(n,k,s,0)
    print('Case #{}: {}'.format(i+1,ans))