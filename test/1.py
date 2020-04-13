class A:
    test = 1
    def __init__(self, t):
        print(self.test)
        self.test = 2


a = A(1)
print(a.test)
print(A.test)
b = A(2)
print(b.test)
print(A.test)