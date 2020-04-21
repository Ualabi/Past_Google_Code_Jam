T = int(input())
for i in range(T):
    W, H, L, U, R, D = map(int,input().split())
    
    if H == 1 or W == 1 or (L == 1 and U == 1):
        print('Case #{}: 0.0'.format(i+1))
        continue
    
    new = []
    for x in range(H):
        pst, new = new, []
        for y in range(W):
            if U-1<=x and x<D and L-1<=y and y<R:   new.append(0)
            else:                                   new.append(True)
                
        for y in range(W):
            if new[y]:
                if x == 0:
                    if y == 0:      new[y] = 1
                    else:           new[y] = new[y-1]/2
                elif x == H-1:
                    if y == 0:      new[y] = pst[y]/2
                    elif y == W-1:  new[y] = new[y-1] + pst[y]
                    else:           new[y] = new[y-1] + pst[y]/2
                else:
                    if y == 0:      new[y] = pst[y]/2
                    elif y == W-1:  new[y] = new[y-1]/2 + pst[y]
                    else:           new[y] = new[y-1]/2 + pst[y]/2
            else:
                continue
    
    print('Case #{}: {}'.format(i+1,new[-1]))

    '''
    4 2 0.2343749999999999
    5 1 0.09375
    6 0 0.015625
    8 1 0.017578125000000017

0  -  [1, 0.5, 0.25]
1  -  [0.5, 0.5, 0.375]
2  -  [0.25, 0.375, 0.375]
3  -  [0.125, 0.25, 0.3125]
4  -  [0.0625, 0.15625, 0.234375]
5  -  [0.03125, 0.09375]
6  -  [0.015625]
0  -  [1, 0.5]
1  -  [0.5, 0.5]
2  -  [0.25, 0.375]
3  -  [0.125, 0.25]
4  -  [0.0625, 0.15625]
5  -  [0.03125, 0.09375]
6  -  [0.015625, 0.0546875]
7  -  [0.0078125, 0.03125]
8  -  [0.00390625, 0.01953125]
    '''