T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    # arr 네방향 0으로 패딩해서 둘러쌈
    arr = [[0]*(N+2) for _ in range(N+2)]
    # [1] 초기 돌 놓기
    m = N//2
    arr[m][m] = arr[m+1][m+1] = 2
    arr[m+1][m] = arr[m][m+1] = 1

    # [2] 흑돌 백돌 입력 받아서 처리
    for _ in range(M):
        si, sj, d = map(int, input().split())
        # 8방향 처리
        for di, dj in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
            # 해당 방향으로 뻗어나가면서 처리
            tlst = []
            for mul in range(1, N):
                ni, nj = si+di*mul, sj+dj*mul
                arr[si][sj] = d
                if arr[ni][nj] == 0:   # 범위밖
                    break
                elif arr[ni][nj] != d:   # 다른 돌인 경우 뒤집기 후보에 추가
                    tlst.append((ni, nj))
                else:  # 같은 돌이면 후보들을 뒤집고 종료
                    while tlst:
                        ti, tj = tlst.pop()
                        arr[ti][tj] = d
                    break

        bcnt = wcnt = 0
        for lst in arr:
            bcnt += lst.count(1)
            wcnt += lst.count(2)

    print(f'#{tc} {bcnt} {wcnt}')