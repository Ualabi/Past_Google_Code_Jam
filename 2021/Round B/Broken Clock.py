# https://codingcompetitions.withgoogle.com/codejam/round/0000000000435baf/00000000007ae694

op = ((0,1,2),(0,2,1),(1,0,2),(1,2,0),(2,0,1),(2,1,0))
vl = 432*(10**11)
dg = 12*(10**10)
md = 10**9

T = int(input())
for t in range(T):
    A = list(map(int,input().split()))
    
    flag = False
    for i,j,k in op:
        h,m,s = A[i], A[j], A[k]

        if m%12 != s%12:
            continue
        
        for H in range(12):
            l = h-H*30*dg
            r = (vl+m-l)%vl
            
            ticks = r//11
            M = (ticks//md)//60
            S = (ticks//md)%60
            MS= ticks%md
            
            if 330*dg < r or r%11 != 0 or 60 <= M:
                continue

            sec = (ticks*720)%vl
            pos = ((vl+m-12*ticks)%vl+sec)%vl
            
            if pos == s:
                flag = True
                print('Case #{}: {} {} {} {}'.format(t+1,H,M,S,MS))
                break
        
        if flag: break