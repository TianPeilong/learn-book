from heapq import heappush

class heap:
    def __init__(self):
        self.heap = [0]
        self.size = 0

    def insert(self, item):
        self.heap.append(item)
        self.size += 1
        self._float(self.size)
    
    def _float(self, k):
        while k // 2 > 0:
            parent = k // 2
            if self.heap[parent] > self.heap[k]:
                self.heap[parent], self.heap[k] = self.heap[k], self.heap[parent]
            else:
                break

    def pop(self):
        if self.size < 1:
            return None
        item = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        self._sink(1)
        return item
    
    def _sink(self, k):
        while 2 * k <= self.size:
            mi = self._minindex(k)
            if self.heap[k] > self.heap[mi]:
                self.heap[k], self.heap[mi] = self.heap[mi], self.heap[k]
                k = mi
            else:
                break
                
    def _minindex(self, k):
        if 2 * k + 1 > self.size:
            return 2 * k
        elif self.heap[2*k] < self.heap[2*k+1]:
            return 2 * k
        else:
            return 2 * k + 1

arr = [1,9,3,5,7,2]


h = heap()
ph = []
for a in arr:
    h.insert(a)
    heappush(ph, a)

print(h.heap)
print(ph)
