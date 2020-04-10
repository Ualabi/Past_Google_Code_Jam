# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/0000000000209a9e

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
            if r == 0: #Normal
                pass
            elif r == 1: #Inviertido
                aux = ''
                for x in guess:
                    aux += '1' if x=='0' else '0'
                guess = aux

            elif r == 2: #Espejo
                guess = guess[::-1]
            elif r == 3: #Inertido espejo
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
    s = ['']*B

    c = 1
    dct = {}
    ki, kd = None, None

    left, right = 1, B
    while left < right and (not ki or not kd):
        l = judgeSystem(left)
        r = judgeSystem(right)
        dct[left] = l+r

        if l==r and not ki: 
            s[left-1], s[B-left] = '0', '0'
            ki = left
            kx = l
        if l!=r and not kd: 
            s[left-1], s[B-left] = '0', '1'
            kd = left
            ky = l

        left, right = left+1, right-1
        c += 2
    #print(dct)

    if right < left and (not ki or not kd): # Todas las parejas de espejos fueron iguales o diferentes
        d = 0
        left = 1
        while d < B//10:
            l = judgeSystem(left)
            if l == dct[left][0]:   # Si es igual, entonces 5 izquierdas son iguales a sus espejos
                for x in range(5):
                    s[left+x-1] = dct[left+x][0]
                    s[B-left-x] = dct[left+x][1]
            else:                   # Si es igual, entonces los 5 izquierdas y espejos son sus inversos
                for x in range(5): 
                    s[left+x-1] = '1' if dct[left+x][0]=='0' else '0'
                    s[B-left-x] = '1' if dct[left+x][1]=='0' else '0'
            d += 1
            left += 5
        #print(s)
        l = judgeSystem(''.join(s))
        if l == 'Y':
            return None
        elif l == 'N':
            exit()
    else:                           # Existen 2 parejas de iguales y diferentes
        while(c%10 != 1):
            l = judgeSystem(left)
            r = judgeSystem(right)
            c += 2

        d = 1
        left = 1
        if max(ki,kd)%5 == 0:
            maxi = max(ki,kd)-5+1 
        else:
            maxi = max(ki,kd) - max(ki,kd)%5 +1

        if maxi > 1:
            kx = judgeSystem(ki)
            ky = judgeSystem(kd)
            kk = kx+ky
            c += 2

            while True:
                if d == maxi:
                    break
                elif d == 1:
                    if ki == 1:     flag = kx == dct[1][0]
                    elif kd == 1:   flag = ky == dct[1][0]
                else:
                    flag = judgeSystem(d) == dct[d][0]
                    c += 1

                for x in range(d,min(d+5,max(ki,kd))):
                    if flag:    # Si don iguales y los pasamos
                        if kk == '00':      # Normal
                            s[x-1] = dct[x][0]
                            s[B-x] = dct[x][1]
                        elif kk == '01':    # Espejo
                            s[x-1] = dct[x][1]
                            s[B-x] = dct[x][0]
                        elif kk == '10':    # Inverso espejo
                            s[x-1] = '1' if dct[x][1]=='0' else '0'
                            s[B-x] = '1' if dct[x][0]=='0' else '0'
                        elif kk == '11':    # Inverso
                            s[x-1] = '1' if dct[x][0]=='0' else '0'
                            s[B-x] = '1' if dct[x][1]=='0' else '0'
                    else:       # Si son diferentes e invertimos
                        if kk == '00':      # Inverso
                            s[x-1] = '1' if dct[x][0]=='0' else '0'
                            s[B-x] = '1' if dct[x][1]=='0' else '0'
                        elif kk == '01':    # Inverso Espejo
                            s[x-1] = '1' if dct[x][1]=='0' else '0'
                            s[B-x] = '1' if dct[x][0]=='0' else '0'
                        elif kk == '10':    # Espejo
                            s[x-1] = dct[x][1]
                            s[B-x] = dct[x][0]
                        elif kk == '11':    # Normal
                            s[x-1] = dct[x][0]
                            s[B-x] = dct[x][1]
                d += 5
            
            while(c%10 != 1):
                l = judgeSystem(1)
                c += 1
        #print(s)

        while d <= B//2:
            kx = judgeSystem(ki)
            ky = judgeSystem(kd)
            kk = kx+ky
            c += 2

            for x in range(d,min(B//2+1,d+4)):
                l = judgeSystem(x)
                r = judgeSystem(B-x+1)
                c += 2

                if kk == '00':      # Normal
                    s[x-1] = l
                    s[B-x] = r
                elif kk == '01':    # Espejo
                    s[x-1] = r
                    s[B-x] = l
                elif kk == '10':    # Inverso espejo
                    s[x-1] = '1' if r=='0' else '0'
                    s[B-x] = '1' if l=='0' else '0'
                elif kk == '11':    # Inverso
                    s[x-1] = '1' if l=='0' else '0'
                    s[B-x] = '1' if r=='0' else '0'
            
            left, right = left+1, right-1
            d += 4
    
    a = ['']*B
    for x in range(1, B//2 + 1):
        if kk == '00':      # Normal
            a[x-1] = s[x-1]
            a[B-x] = s[B-x]
        elif kk == '01':    # Espejo
            a[x-1] = s[B-x]
            a[B-x] = s[x-1]
        elif kk == '10':    # Inverso espejo
            a[x-1] = '1' if s[B-x]=='0' else '0'
            a[B-x] = '1' if s[x-1]=='0' else '0'
        elif kk == '11':    # Inverso
            a[x-1] = '1' if s[x-1]=='0' else '0'
            a[B-x] = '1' if s[B-x]=='0' else '0'
    
    #print(''.join(s))
    print(''.join(a))
    l = judgeSystem(''.join(a))
    if l == 'Y':
        return None
    elif l == 'N':
        quit()

if B==10:
    a = []
    for x in range(10):
        a.append(judgeSystem(x+1))
    
    aux = judgeSystem(''.join(a))
    if aux == 'T':
        #continue
        pass
    elif aux == 'N':
        exit()
else:
    solve(B)

""" for w in range(2**20):
    guess = ''
    r = w
    for x in range(20):
        if r%2 == 1:
            guess += '1'
        else:
            guess += '0'
        
        r = r//2

    count = 1

    #print(w,' - ',guess)

    solve(B) """
