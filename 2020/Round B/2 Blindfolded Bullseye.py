# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fef2/00000000002d5b63

def ask(x, y):
    print('{} {}'.format(int(x),int(y)))
    ans = input()
    if (ans == 'WRONG'):
        quit()
    if (ans == 'CENTER'):
        return 0
    if (ans == 'HIT'):
        return 1
    return -1

def func(x, y, dx, dy):
    l = 0
    r = 2*10**9 + 1
    while (r - l > 1):
        h = int((l + r) / 2)
        nx = x + h * dx
        ny = y + h * dy
        if (abs(nx) > 10**9 or abs(ny) > 10**9):
            r = h
            continue
        t = ask(nx, ny)
        if (t == 0):
            return -1
        if (t == 1):
            l = h
        else:
            r = h
    return l

def solve():
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    JMP = 250000000
    for i in range(-JMP*3, 3*JMP+1, JMP):
        for j in range(-JMP*3, 3*JMP+1, JMP):
            t = ask(i, j)
            if (t == 0):
                return None
            if (t == 1):
                x = i
                y = j
                break

    f = [None]*4
    for d in range(4):
        f[d] = func(x, y, dx[d], dy[d])
        if (f[d] == -1):
            return None

    xn = ((f[2] - f[3])//2) + x
    yn = ((f[0] - f[1])//2) + y
    
    if ask(xn, yn) == 0:    return None
    else:                   quit()

T,A,B = map(int,input().split())
for i in range(T):
    solve()
