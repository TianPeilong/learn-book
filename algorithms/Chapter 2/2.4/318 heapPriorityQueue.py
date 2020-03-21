class HeapPriorityQueue:
    def __init__(self):
        self.heap = [0]
    
    def insert(self, item):
        self.heap.append(item)
        self._swim(len(self.heap)-1)

    def _swim(self, k):
        while k // 2 > 0:
            p = k // 2
            if self.heap[p] < self.heap[k]:
                self.heap[p], self.heap[k] = self.heap[k], self.heap[p]
            else:
                break
    def pop(self):
        if len(self.heap) == 1:
            return None
        item = self.heap[1]
        end = self.heap.pop()
        if len(self.heap) > 1:
            self.heap[1] = end
            self._sink(1)
        return item

    def _sink(self, k):
        n = len(self.heap) - 1
        while 2*k <= n:
            j = 2 * k
            if j < n and self.heap[j] < self.heap[j+1]:
                j += 1
            if self.heap[k] < self.heap[j]:
                self.heap[k], self.heap[j] = self.heap[j], self.heap[k]
                k = j
            else:
                break

    def empty(self):
        return len(self.heap) == 1
        
        