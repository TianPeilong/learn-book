class KthLargest:

    def __init__(self, k: int, nums):
        self.k = k
        self.heap = [0]
        while len(nums) > 0 and len(self.heap) <= k:
            cur = nums.pop()
            self.heap.append(cur)
            self.swim(self.heap, len(self.heap)-1)
        while len(nums) > 0:
            cur = nums.pop()
            if cur > self.heap[1]:
                self.heap[1] = cur
                self.sink(self.heap, 1)

    def swim(self, arr, m):
        while m > 1:
            pre = m // 2
            if arr[pre] > arr[m]:
                arr[pre], arr[m] = arr[m], arr[pre]
                m = pre
            else:
                break

    def sink(self, arr, m):
        end = len(arr)-1
        while 2 * m <= end:
            c = 2 * m
            if c < end and arr[c] > arr[c+1]:
                c += 1
            if arr[c] < arr[m]:
                arr[c], arr[m] = arr[m],arr[c]
                m = c
            else:
                break
                
        
    def add(self, val: int) -> int:
        if len(self.heap) < self.k + 1:
            self.heap.append(val)
            self.swim(self.heap, len(self.heap)-1)
        elif val > self.heap[1]:
            self.heap[1] = val
            self.sink(self.heap, 1)
        return self.heap[1]


'''
import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        n = len(nums)
        heapq.heapify(nums)
        self.heap = nums
        while n > k:
            heapq.heappop(self.heap)
            n -= 1
        self.n = n
        
    def add(self, val: int) -> int:
        if self.n < self.k:
            heapq.heappush(self.heap, val)
            self.n += 1
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val)
        return self.heap[0]
'''
        


# Your KthLargest object will be instantiated and called as such:
k = 2
nums = [0]

obj = KthLargest(k, nums)
add_nums = [-1,1,-2,-4,3]
for i in add_nums:
    print(obj.add(i))