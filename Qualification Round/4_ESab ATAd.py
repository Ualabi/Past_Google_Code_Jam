# https://codingcompetitions.withgoogle.com/codejam/round/000000000019fd27/0000000000209a9e

T, B = map(int, input().split())
for tt in range(T):
    ans = ['']*B
    sub = ['']*B
    
    c = 1   # Counter of times we have asked
    dct = {}
    ki, kd = None, None # Indexes of the left number of the pair of equal, different numbers 
    
    left, right = 1, B
    while left < right: # Search for a pair of equal numbers and a pair of different numbers
        print(left)
        l = input()
        print(right)
        r = input()
        c += 2
        
        dct[left] = l+r
        
        if not ki and l==r: ki = left
        if not kd and l!=r: kd = left
        if ki and kd:       break       # If you have it already, break the while
        left, right = left+1, right-1   # Change the pointers
    
    while(c%10 != 1): # Set again the counter in a number%10 == 1
        print(1)
        l = input()
        c += 1
    
    if not ki or not kd: # This means that all the pairs have equal numbers or different
        left = 1
        while left <= B//2:
            print(left)
            l = input()
            if l == dct[left][0]: # If the first is equal, then the rest as well (5 left, 5 right)
                for x in range(5):
                    ans[left+x-1] = dct[left+x][0]
                    ans[B-left-x] = dct[left+x][1]
            else:
                for x in range(5): 
                    ans[left+x-1] = '1' if dct[left+x][0]=='0' else '0'
                    ans[B-left-x] = '1' if dct[left+x][1]=='0' else '0'
            left += 5
    else: # This means that there are the 2 pairs of equal and diff numbers
        left = 1
        maxi = max(ki,kd)+1
        maxi -= 5 if max(ki,kd)%5 == 0 else max(ki,kd)%5 # Max number for the while

        if 1 < maxi: # If maxi is 1, there is not need to use dct for the first values
            print(ki)
            kx = input()
            print(kd)
            ky = input()
            c += 2
            
            kk = kx+ky
            while left < maxi:
                if left == 1:   #First case, dont ask for the value
                    if ki == 1:     flag = kx == dct[1][0]
                    elif kd == 1:   flag = ky == dct[1][0]
                else:
                    print(left)
                    l = input()
                    flag = l == dct[left][0]
                    c += 1
                    
                for x in range(left,left+5):
                    if flag:    # If both are equal, we pass
                        if kk == '00':      # Normal
                            sub[x-1] = dct[x][0]
                            sub[B-x] = dct[x][1]
                        elif kk == '01':    # Mirror
                            sub[x-1] = dct[x][1]
                            sub[B-x] = dct[x][0]
                        elif kk == '10':    # Inverse Mirror
                            sub[x-1] = '1' if dct[x][1]=='0' else '0'
                            sub[B-x] = '1' if dct[x][0]=='0' else '0'
                        elif kk == '11':    # Inverse
                            sub[x-1] = '1' if dct[x][0]=='0' else '0'
                            sub[B-x] = '1' if dct[x][1]=='0' else '0'
                    else:       # We do the operation inverse
                        if kk == '00':      # Inverse
                            sub[x-1] = '1' if dct[x][0]=='0' else '0'
                            sub[B-x] = '1' if dct[x][1]=='0' else '0'
                        elif kk == '01':    # Inverse Mirror
                            sub[x-1] = '1' if dct[x][1]=='0' else '0'
                            sub[B-x] = '1' if dct[x][0]=='0' else '0'
                        elif kk == '10':    # Mirrow
                            sub[x-1] = dct[x][1]
                            sub[B-x] = dct[x][0]
                        elif kk == '11':    # Normal
                            sub[x-1] = dct[x][0]
                            sub[B-x] = dct[x][1]
                left += 5
            
            while(c%10 != 1): # Set again the counter in a number%10 == 1
                print(1)
                l = input()
                c += 1
        
        # Now, for the rest of the number we first ask for Ki,Kd
        # So we can know in which case of the random we are
        # We are setting 'sub' in the case that ki, kd are both 0
        while left <= B//2:
            print(ki)
            kx = input()
            print(kd)
            ky = input()
            c += 2
            
            kk = kx+ky
            for x in range(left,min(B//2+1,left+4)):
                print(x)
                l = input()
                print(B-x+1)
                r = input()
                c += 2
                
                if kk == '00':      # Normal
                    sub[x-1] = l
                    sub[B-x] = r
                elif kk == '01':    # Mirror
                    sub[x-1] = r
                    sub[B-x] = l
                elif kk == '10':    # Inverse Mirror
                    sub[x-1] = '1' if r=='0' else '0'
                    sub[B-x] = '1' if l=='0' else '0'
                elif kk == '11':    # Inverse
                    sub[x-1] = '1' if l=='0' else '0'
                    sub[B-x] = '1' if r=='0' else '0'
            left += 4
        
        # Now, we pass sub to the actual case of the bits
        # For that we need to look at the case of KK
        for x in range(1, B//2+1):
            if kk == '00':      # Normal
                ans[x-1] = sub[x-1]
                ans[B-x] = sub[B-x]
            elif kk == '01':    # Mirror
                ans[x-1] = sub[B-x]
                ans[B-x] = sub[x-1]
            elif kk == '10':    # Inverse Mirror
                ans[x-1] = '1' if sub[B-x]=='0' else '0'
                ans[B-x] = '1' if sub[x-1]=='0' else '0'
            elif kk == '11':    # Inverse
                ans[x-1] = '1' if sub[x-1]=='0' else '0'
                ans[B-x] = '1' if sub[B-x]=='0' else '0'
    
    print(''.join(ans)) # Print the value
    aux = input()
    if aux == 'T':      continue
    elif aux == 'N':    exit()
