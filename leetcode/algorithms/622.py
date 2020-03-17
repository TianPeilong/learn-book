class MyCircularQueue(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.inner = [0] * k
        self.total = k
        self.head = 0
        self.count = 0
        

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.count >= self.total:
            return False
        tail = (self.head + self.count) % self.total
        self.inner[tail] = value
        self.count += 1
        return True

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.count <= 0:
            return False
        self.head = (self.head + 1) % self.total
        self.count -= 1
        return True
        
        

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        return -1 if self.count <= 0 else self.inner[self.head]

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        return -1 if self.count <= 0 else self.inner[(self.head + self.count - 1) % self.total]


    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        return self.count <= 0
        

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        return self.count == self.total
        


# Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(3)
param_1 = obj.enQueue(1)
param_1 = obj.enQueue(2)
param_1 = obj.enQueue(3)
param_1 = obj.enQueue(4)
param_2 = obj.deQueue()
param_3 = obj.Front()
param_4 = obj.Rear()
param_5 = obj.isEmpty()
param_6 = obj.isFull()