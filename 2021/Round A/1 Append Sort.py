# https://codingcompetitions.withgoogle.com/codejam/round/000000000043585d/00000000007549e5

T = int(input())
for t in range(T):
    N = int(input())
    X = list(map(int,input().split()))
    
    ans, past, lenp = 0, 0, 1
    for n in range(N):
        curr = X[n]
        lenc = len(str(curr))

        if past < curr:         # past < curr
            past = curr

        elif lenp == lenc:      # lenp == lenc
            past = curr*10

        else:                   # pd > nd
            pw = 10**(lenp-lenc)
            l = past//pw
            r = curr*pw
            
            if curr < l:
                past = r*10
            elif curr > l:
                past = r
            elif past-r+1 == pw:
                past = r*10
            else:
                past += 1

        lenp = len(str(past))
        ans += lenp-lenc

    print('Case #{}: {}'.format(t+1,ans))