import numpy as np
import heapq

l1 = [[i,j,i+j] for i in range(10) for j in range(10)]

print(l1)

heapq.heapify(l1)

print(l1)