# https://codingcompetitions.withgoogle.com/codejam/round/000000000043580a/00000000006d0a5c

T = int(input())
for t in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    
    ans = 0
    for x in range(N-1):
        minim = float('inf')
        index = x
        for y in range(x,N):
            if arr[y] < minim:
                minim = arr[y]
                index = y
        ans += index-x+1

        for y in range((index-x+1)//2):
            arr[x+y],arr[index-y] = arr[index-y],arr[x+y]

    print("case #{}: {}".format(t+1,ans))