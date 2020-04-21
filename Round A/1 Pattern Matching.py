# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd74/00000000002b3034

T = int(input())

for i in range(T):
    n = int(input())
    sl, sr = "", ""
    mid = ""
    ok = True
    for j in range(n):
        s = input()
        x = 0
        while (s[x] != '*'):
            if (x < len(sl)):
                ok &= (sl[x] == s[x])
            else:
                sl += s[x]
            x += 1
        
        y = 0
        while (s[len(s) - y - 1] != '*'):
            if (y < len(sr)):
                ok &= (sr[y] == s[len(s) - y - 1])
            else: 
                sr += s[len(s) - y - 1]
            y += 1

        for k in range(x+1, len(s)-y-1):
            if (s[k] != '*'):
                mid += s[k]

    if ok:
        sr = sr[::-1]
        word = sl+mid+sr
    else:
        word = '*'
    
    print("Case #{}: {}".format(i+1,word))
