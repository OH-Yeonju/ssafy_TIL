T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    lst.sort()
    minV = 1000
    for i in range(N-2):
        for j in range(i+1, N-1):
            if lst[i] != lst[i+1] and lst[j] != lst[j+1]:
                A = i+1
                B = j-i
                C = N-j-1
                if A*B*C !=0 and A<=N//2 and B<=N//2 and C<=N//2:
                    k = max(A, B, C) - min(A, B, C)
                    if minV > k:
                        minV = k
    if minV == 1000:
        minV = -1
    print(f'#{tc} {minV}')