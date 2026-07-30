n = int(input())

arr = []
for i in range(n):
    l, r = map(int, input().split())
    arr.append([l, r])

import heapq

heap = []

arr.sort(key=lambda x: x[0])

for i in range(n):
    if not heap or heap[0] >= arr[i][0]:
        heapq.heappush(heap, arr[i][1])
    else:
        heapq.heappop(heap)
        heapq.heappush(heap, arr[i][1])
        
print(len(heap))
