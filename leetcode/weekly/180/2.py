class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.inner = []


    def push(self, x: int) -> None:
        if len(self.inner) < self.maxSize:
            self.inner.append(x)


    def pop(self) -> int:
        if not self.inner:
            return -1
        return self.inner.pop()


    def increment(self, k: int, val: int) -> None:
        max_v = k if k < len(self.inner) else len(self.inner)
        for i in range(max_v):
            self.inner[i] += val

customStack = CustomStack(3)
customStack.push(1)                     
customStack.push(2)                          
customStack.pop()                            
customStack.push(2)                          
customStack.push(3)                          
customStack.push(4)                          
customStack.increment(5, 100)                
customStack.increment(2, 100)                
customStack.pop()                            
customStack.pop()                            
customStack.pop()                            
customStack.pop()                            