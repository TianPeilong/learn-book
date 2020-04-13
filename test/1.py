class A:
    test = None
    def __init__(self, t):
        self.test = t

a = A(1)
print(a.test)
print(A.test)
b = A(2)
print(b.test)
print(A.test)