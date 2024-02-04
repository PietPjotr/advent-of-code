import sys
import re
import heapq

bots = [tuple(map(int, re.findall("-?\d+", line))) for line in sys.stdin]
events = []

for x, y, z, r in bots:
    d = abs(x) + abs(y) + abs(z)
    heapq.heappush(events, (max(0, d - r), 1))
    heapq.heappush(events, (d + r + 1, -1))

count = 0
maxCount = 0
result = 0

while events:
    dist, e = heapq.heappop(events)
    count += e
    if count > maxCount:
        result = dist
        maxCount = count

print(result)
