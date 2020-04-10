import random
random.seed()

guess = ''
B = 100
count = 1
for x in range(B):
    guess += '1' if random.random()>0.5 else '0'

def judgeSystem(pos):
    global guess, B, count
    if type(pos) == int:            
        if count%10 == 1:
            r = random.choice([0,1,2,3])
            if r == 0:      # Normal
                pass
            elif r == 1:    # Inverse
                aux = ''
                for x in guess:
                    aux += '1' if x=='0' else '0'
                guess = aux

            elif r == 2:    # Mirror
                guess = guess[::-1]
            elif r == 3:    #Inverse Mirror
                aux = ''
                for x in guess:
                    aux += '1' if x=='0' else '0'
                guess = aux[::-1]
            print(' - ',guess)
        print(count,' - ',pos,' , ',guess[pos-1])
        count += 1
        return guess[pos-1]

    elif type(pos) == str:
        if pos == guess:
            print('Y, ',pos,count)
            return 'Y'
        else:
            print('N, ',pos,' - ',guess)
            return 'N'

def solve(B):
    ans = ['']*B
    sub = ['']*B
    
    c = 1
    dct = {}
    ki, kd = None, None
    
    left, right = 1, B
    while left < right:
        l = judgeSystem(left)
        r = judgeSystem(right)
        dct[left] = l+r
        c += 2
        
        dct[left] = l+r
        
        if not ki and l==r: ki = left
        if not kd and l!=r: kd = left
        if ki and kd:       break
        left, right = left+1, right-1
    
    while(c%10 != 1):
        l = judgeSystem(1)
        c += 1
    
    if not ki or not kd:
        left = 1
        while left <= B//2:
            l = judgeSystem(left)
            if l == dct[left][0]:
                for x in range(5):
                    ans[left+x-1] = dct[left+x][0]
                    ans[B-left-x] = dct[left+x][1]
            else:
                for x in range(5): 
                    ans[left+x-1] = '1' if dct[left+x][0]=='0' else '0'
                    ans[B-left-x] = '1' if dct[left+x][1]=='0' else '0'
            left += 5
    else:
        left = 1
        maxi = max(ki,kd)+1
        maxi -= 5 if max(ki,kd)%5 == 0 else max(ki,kd)%5

        if 1 < maxi:
            kx = judgeSystem(ki)
            ky = judgeSystem(kd)
            c += 2
            
            kk = kx+ky
            while left < maxi:
                if left == 1:
                    if ki == 1:     flag = kx == dct[1][0]
                    elif kd == 1:   flag = ky == dct[1][0]
                else:
                    flag = judgeSystem(left) == dct[left][0]
                    c += 1
                    
                for x in range(left,left+5):
                    if flag:    # Si don iguales y los pasamos
                        if kk == '00':      # Normal
                            sub[x-1] = dct[x][0]
                            sub[B-x] = dct[x][1]
                        elif kk == '01':    # Espejo
                            sub[x-1] = dct[x][1]
                            sub[B-x] = dct[x][0]
                        elif kk == '10':    # Inverso espejo
                            sub[x-1] = '1' if dct[x][1]=='0' else '0'
                            sub[B-x] = '1' if dct[x][0]=='0' else '0'
                        elif kk == '11':    # Inverso
                            sub[x-1] = '1' if dct[x][0]=='0' else '0'
                            sub[B-x] = '1' if dct[x][1]=='0' else '0'
                    else:       # Si son diferentes e invertimos
                        if kk == '00':      # Inverso
                            sub[x-1] = '1' if dct[x][0]=='0' else '0'
                            sub[B-x] = '1' if dct[x][1]=='0' else '0'
                        elif kk == '01':    # Inverso Espejo
                            sub[x-1] = '1' if dct[x][1]=='0' else '0'
                            sub[B-x] = '1' if dct[x][0]=='0' else '0'
                        elif kk == '10':    # Espejo
                            sub[x-1] = dct[x][1]
                            sub[B-x] = dct[x][0]
                        elif kk == '11':    # Normal
                            sub[x-1] = dct[x][0]
                            sub[B-x] = dct[x][1]
                left += 5
            
            while(c%10 != 1):
                l = judgeSystem(1)
                c += 1
        
        while left <= B//2:
            kx = judgeSystem(ki)
            ky = judgeSystem(kd)
            c += 2
            
            kk = kx+ky
            for x in range(left,min(B//2+1,left+4)):
                l = judgeSystem(x)
                r = judgeSystem(B-x+1)
                c += 2
                
                if kk == '00':      # Normal
                    sub[x-1] = l
                    sub[B-x] = r
                elif kk == '01':    # Espejo
                    sub[x-1] = r
                    sub[B-x] = l
                elif kk == '10':    # Inverso espejo
                    sub[x-1] = '1' if r=='0' else '0'
                    sub[B-x] = '1' if l=='0' else '0'
                elif kk == '11':    # Inverso
                    sub[x-1] = '1' if l=='0' else '0'
                    sub[B-x] = '1' if r=='0' else '0'
            left += 4
        
        for x in range(1, B//2+1):
            if kk == '00':      # Normal
                ans[x-1] = sub[x-1]
                ans[B-x] = sub[B-x]
            elif kk == '01':    # Espejo
                ans[x-1] = sub[B-x]
                ans[B-x] = sub[x-1]
            elif kk == '10':    # Inverso espejo
                ans[x-1] = '1' if sub[B-x]=='0' else '0'
                ans[B-x] = '1' if sub[x-1]=='0' else '0'
            elif kk == '11':    # Inverso
                ans[x-1] = '1' if sub[x-1]=='0' else '0'
                ans[B-x] = '1' if sub[B-x]=='0' else '0'
    
    aux = judgeSystem(''.join(ans))
    if aux == 'T':      pass
    elif aux == 'N':    exit()

solve(B)
