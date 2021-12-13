import heqpq

R, C = map(int, input().split())
seat = []
for _ in range(R):
    seat.append(input())
    

chair, people = [], []
seated = []*10000
finished = [False] * 10000

answer = 0

chair_idx = []
hq = []

for i in range(R):
    for j in range(C):
        if seat[i][j] == 'X':
            people.append((i,j))
        elif seat[i][j] == 'L':
            chair.append((i,j))

for p_idx, person in enumerate(people):
    px, py = person[0], person[1]
    
    for c_idx, ch in enumerate(chair):
        cx, cy = ch[0], ch[1]
        dist = (px - cx) ** 2 + (py - cy) ** 2
        haepq.heappush(hq, (dist, p_idx, c_idx))
        
print(hq)