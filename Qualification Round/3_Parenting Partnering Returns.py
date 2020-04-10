# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/000000000020bdf9

def getSol(a,mydict):
    nums = []
    for y in sorted(mydict):
        if len(mydict[y]) >= 3:
            return 'IMPOSSIBLE'
        elif len(mydict[y]) == 2:
            [l1,l2] = mydict[y]
            if l1[1] <= l2[1]:
                nums.append(l1)
                nums.append(l2)
            else:
                nums.append(l2)
                nums.append(l1)
        else:
            nums.append(mydict[y][0])

    C = [True]*1440
    J = [True]*1440
    
    mystr = ['']*a
    for [y,z,t] in nums: 
        for q in range(y,z):
            if C[q] == False:
                break
        if C[q]:
            for q in range(y,z):
                C[q] = False
            mystr[t] = 'C'
        else:
            for q in range(y,z):
                if J[q] == False:
                    break    
            if J[q]:
                for q in range(y,z):
                    J[q] = False
                mystr[t] = 'J'
            else:
                return 'IMPOSSIBLE'
    return ''.join(mystr)

T = int(input())
for x in range(T):
    a = int(input())
    mydict = {}
    for y in range(a):
        [q,w] = list(map(int,input().split()))
        mydict[q] = mydict.get(q, []) + [[q,w,y]]
    
    print("Case #{}: {}".format(x+1, getSol(a,mydict)))
