# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fef2/00000000002d5b62

def solve(x,y,h):
    if x == 0 and y == 0:
        return ""
    if (abs(x)%2 == abs(y)%2):
        return "IMPOSSIBLE"
    if (h >= 50):
        return "IMPOSSIBLE"
    if (x%2 == 0):
        x = x//2
        can = [[(y-1)//2, 'N'], [(y+1)//2, 'S']]
        for t in can:
            if (x == 0 and t[0] == 0):
                to = t
                break
            if (abs(x)%2 != abs(t[0])%2):
                to = t
        ans = solve(x, to[0], h+1)
        if (ans == "IMPOSSIBLE"):
            return ans
        ans = to[1] + ans
        return ans
    if (y%2 == 0):
        y = y//2
        can = [[(x-1)//2, 'E'], [(x+1)//2, 'W']]
        for t in can:
            if (y == 0 and t[0] == 0):
                to = t
                break
            if (abs(y) % 2 != abs(t[0]) % 2):
                to = t
        ans = solve(to[0], y, h+1)
        if (ans == "IMPOSSIBLE"):
            return ans
        ans = to[1] + ans
        return ans
    return ""

T = int(input())
for i in range(T):
    j, k = map(int,input().split())
    ans = solve(j,k,0)
    print('Case #{}: {}'.format(i+1,ans))
