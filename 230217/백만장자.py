# T = int(input())
#
# for tc in range(1, T+1):
#     N = int(input())
#     lst = list(map(int, input().split()))
#
#     ans = mx = 0
#     for n in lst:
#         if mx>n:
#             ans += mx-n
#         else:
#             mx = n

    # i = 0
    # ans = 0
    # while i<N:
    #     # [1] i~ 끝까지 최대값의 idx찾기
    #     i_mx = i
    #     for j in range(i+1, N):
    #         if lst[i_mx]<lst[j]:
    #             i_mx = j
    #
    #     # [2] i~i_mx까지의 최대값과의 차이 누적
    #     for j in range(i, i_mx):
    #         ans += lst[i_mx]-lst[j]
    #
    #     i = i_mx + 1



    # print(f'#{tc} {ans}')


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))[::-1]

    ans = mx = 0
    for n in lst:
        if mx > n:
            ans += mx - n
        else:
            mx = n

    print(f'#{test_case} {ans}')