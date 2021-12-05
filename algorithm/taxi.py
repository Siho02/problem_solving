nodes = 6
start = 4
A = 6
B = 2
fare_lst = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]

import heapq



def solution(n, s, a, b, fares):

    link = [[] for _ in range(n+1)]

    for dep, arr, weight in fares:
        link[dep].append((weight, arr))
        link[arr].append((weight, dep))
    print('link = ', link)
    
    #최소 거리 계산을 위한 다익스트라 함수
    def dijkstra(start):
        dist = [float('inf')] * (n+1)
        dist[start] = 0
        heap = []
        heapq.heappush(heap, (0, start))

        while heap:
            value, destination = heapq.heappop(heap)

            if dist[destination] < value:
                continue

            for v, d in link[destination]:
                next_val = value + v
                if dist[d] > next_val:
                    dist[d] = next_val
                    heapq.heappush(heap, (next_val, d))
        
        return dist


    dp = [[]] + [dijkstra(i) for i in range(1, n+1)]
    print(dp)

    answer = float('inf')

    for i in range(1, n+1):
        answer = min(dp[i][a] + dp[i][b] + dp[i][s], answer)

    return answer



answer = solution(nodes, start, A, B, fare_lst)

print(answer)