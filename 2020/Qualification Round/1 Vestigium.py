# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/000000000020993c

T = int(input())

for x in range(T):
    a = int(input())
    m = []
    for y in range(a):
        m.append(list(map(int,input().split())))
    
    q, w, e = 0, 0, 0
    for y in range(a):
        q += m[y][y]
        
        set1, set2 = set(), set()
        for z in range(a):
            set1.add(m[y][z])
            set2.add(m[z][y])
        
        w += 1 if a - len(set1) else 0
        e += 1 if a - len(set2) else 0
    
    print("Case #{}: {} {} {}".format(x+1, q, w, e))
