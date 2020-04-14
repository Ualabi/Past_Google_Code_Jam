# Link: https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd74/00000000002b1355

def getField(arr,r,c):
    follow = set()
    field = {}
    real = 0
    for x in range(r):
        for y in range(c):
            real += arr[x][y]
            # aux = {'up', 'left', 'down', 'right'}
            aux = [-1,-1,-1,-1]
            if 0 < x:   aux[0] = x-1 #u
            if 0 < y:   aux[1] = y-1 #l
            if x+1 < r: aux[2] = x+1 #d
            if y+1 < c: aux[3] = y+1 #r
            field[(x,y)] = aux
            follow.add((x,y))
    
    return field, follow, real

def getSum(arr, field, actual, diff):
    follow = set()
    dlt = set()
    for (x,y) in actual:
        [xu,yl,xd,yr] = field[(x,y)]
        suma = 0
        cc = 0
        if xu >= 0:
            suma += arr[xu][y]
            cc += 1
        if yl >= 0:
            suma += arr[x][yl]
            cc += 1
        if xd >= 0:
            suma += arr[xd][y]
            cc += 1
        if yr >= 0:
            suma += arr[x][yr]
            cc += 1

        if cc*arr[x][y] < suma:
            diff += arr[x][y]
            dlt.add((x,y))
            
    for (x,y) in dlt:
        arr[x][y] = 0
        [xu,yl,xd,yr] = field[(x,y)]
        if xu >= 0:
            field[(xu,y)][2] = xd
            follow.add((xu,y))
        if yl >= 0:
            field[(x,yl)][3] = yr
            follow.add((x,yl))
        if xd >= 0:
            field[(xd,y)][0] = xu
            follow.add((xd,y))
        if yr >= 0:
            field[(x,yr)][1] = yl
            follow.add((x,yr))
        del field[(x,y)]

    return field, follow-dlt, diff

T = int(input())
for i in range(T):
    r, c = map(int,input().split())
    arr = []
    for ii in range(r):
        aux = list(map(int,input().split()))
        arr.append(aux)
    
    field, follow, real = getField(arr,r,c)
    Total, diff = 0, 0
    while follow:
        Total += real - diff
        field, follow, diff = getSum(arr, field, follow, diff)
                        
    print("Case #{}: {}".format(i+1, Total))
