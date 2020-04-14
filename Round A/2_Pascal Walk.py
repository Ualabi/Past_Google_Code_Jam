# Link: https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd74/00000000002b1353

T = int(input())
for ii in range(T):
    N = int(input())
    levels = []
    lvl, val = 0, 1
    while 2*val < N:
        lvl += 1
        val *= 2
    
    while 0 < val:
        if val + lvl <= N:
            N -= val
            levels.append(lvl)
        else:
            N -= 1
            levels.append('s')
            
        lvl -= 1
        val = val//2
    
    points = []
    side = False
    lvl, val = 0, 1  
    for x in levels[::-1]:
        if x == lvl:
            aux = [(lvl+1,x) for x in range(1,lvl+2)]
            if side:    aux.reverse()
            side = not side
        else:
            aux = [(lvl+1,lvl+1)] if side else [(lvl+1,1)]
        
        points += aux
        lvl += 1
        val *= 2
    
    for x in range(N):
        aux = [(lvl+1,lvl+1)] if side else [(lvl+1,1)]
        points += aux
        lvl += 1
    
    print("Case #{}:".format(ii+1))
    for (x,y) in points:
        print("{} {}".format(x,y))
    
