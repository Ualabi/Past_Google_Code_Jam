# https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d1145

maxim = float('inf')

T = int(input())
for t in range(T):
    X, Y, arr = input().split()
    X = int(X)
    Y = int(Y)
    
    ans = 0
    past = arr[0]
    C,J = [0],[0]
    for l in arr[1:]:
        if l == 'C':
            if past == 'C':
                c = C[-1]
            elif past == 'J':
                c = J[-1]+Y
            else:
                c = min(C[-1], J[-1]+Y)
            j = maxim
            
        elif l == 'J':
            if past == 'C':
                j = C[-1]+X
            elif past == 'J':
                j = J[-1]
            else:
                j = min(J[-1], C[-1]+X)
            c = maxim
            
        else:
            if past == 'C':
                c = C[-1]
                j = C[-1]+X
            elif past == 'J':
                c = J[-1]+Y
                j = J[-1]
            else:
                c = min(C[-1],J[-1]+Y)
                j = min(J[-1],C[-1]+X)

        C.append(c)
        J.append(j)
        past = l
    ans = min(C[-1],J[-1])
    
    print('Case #{}: {}'.format(t+1,ans))