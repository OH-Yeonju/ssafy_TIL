def f(i, k, s, t):   #i:원소, k:집합의 크기, s:i-1까지 고려된 합, t:찾고자 하는 합(목표)
    global cnt
    global fcnt
    fcnt += 1
    if s > t:       # 고려한 원소의 합이 찾는 합보다 큰 경우
        return
    elif s == t:
        cnt += 1
        return
    elif i == k:    # 남은 원소를 고려할 필요가 없는 경우
        # if s == t:
            # for j in range(k):
            #     if bit[j]:
            #         print(A[j], end=' ')
            # print()
            # cnt += 1
        return
    else:
        bit[i] = 1
        f(i+1, k, s+A[i], t)    # A[i] 포함
        bit[i] = 0
        f(i+1, k, s, t)      # A[i] 미포함


# A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = 20
A = [i for i in range(1, N+1)]
key = 10
cnt = 0
fcnt = 0
bit = [0]*N

f(0, N, 0, key)
print(cnt, fcnt)    # 합이 key인 부분집합의 수