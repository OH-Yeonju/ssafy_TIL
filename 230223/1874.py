T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]


    for row in range(N):
        for col in range(N):
            for k in range(M):
