T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    ans = 0
    m = N//2
    # [1] 규칙성을 사용하여 찾은 형태
    # for i in range(N):
    #     for j in range(abs(m-i), N-abs(m-i)):
    #         ans += arr[i][j]

    # [2] 범위
    s = e = m
    for i in range(N):
        for j in range(s, e+1):
            ans += arr[i][j]
        # s, e 재조정
        if i < m:
            s -= 1
            e += 1
        else:
            s += 1
            e -= 1
    print(f'#{tc} {ans}')