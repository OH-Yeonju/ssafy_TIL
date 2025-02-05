# 고지식한 패턴 검색 알고리즘
p = 'is' #찾을 패턴
t = 'This is a book~!' # 전체 텍스트
M = len(p) # 찾을 패턴의 길이
N = len(t) # 전체 텍스트의 길이

def BruteForce(p, t):
    i = 0 # t의 인덱스
    j = 0 # p의 인덱스
    while j < M and i < N:
        if t[i] != p[j]: # 비교시 같지 않을 때
            i = i - j # j만큼 왔으니 돌아감
            j = -1
        i = i+1 # 같을 시 둘 다  +1
        j = j+1
    if j == M:
        return i - M # 검색 성공
    else:
        return -1 # 검색 실패

