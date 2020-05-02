def solve(A):
    digits = set()
    B = {}
    for x in A:
        B[x[0]] = B.get(x[0],0)+1
        digits.add(x[-1])
    
    C = {}
    for x in B:
        C[B[x]] = x
    
    z = digits - set(B)
    s = z.pop()
    
    for x in sorted(C,reverse=True):
        s += C[x]
    
    return s
    
    
T = int(input())
for i in range(T):
    U = int(input())
    A = []
    for ii in range(10**4):
        a,b = input().split()
        A.append(b)
    ans = solve(A)
    print('Case #{}: {}'.format(i+1,ans))