# https://www.acmicpc.net/problem/15650

from itertools import combinations

N, M = map(int, input().split())

C = combinations(range(1, N+1), M)

for i in C:
    print(' '.join(map(str, i)))