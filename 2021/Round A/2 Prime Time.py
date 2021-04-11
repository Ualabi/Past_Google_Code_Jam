# https://codingcompetitions.withgoogle.com/codejam/round/000000000043585d/00000000007543d8

T = int(input())
for t in range(T):
    M = int(input())
    data = {}
    
    total = 0
    primes = []
    for m in range(M):
        P, N = map(int,input().split())
        primes.append(P)
        data[P] = N
        total += P*N

    m = M-1
    suma, mult = 0, 1
    while mult < total:
        for p in range(data[primes[m]]):
            mult *= primes[m]
            suma += primes[m]
            if total < mult:
                break
        m -= 1 
    
    ans = 0
    for num in range(total-1,total-suma,-1):
        j = 0
        flag = True
        suma, mult = 0, 1
        while 1 < num and j < M:
            cnt = 0
            while num%primes[j] == 0:
                mult *= primes[j]
                suma += primes[j]
                num //= primes[j]
                cnt += 1
            if data[primes[j]] < cnt:
                flag = False
                break
            j += 1

        if num == 1 and flag and mult == total-suma:
            ans = mult
            break
            
    print('Case #{}: {}'.format(t+1, ans))