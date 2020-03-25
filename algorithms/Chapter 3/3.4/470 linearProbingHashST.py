class LinearProbingHashST:
    def __init__(self, m=16):
        self.n = 0
        self.m = m
        self.keys = [None] * 16
        self.vals = [None] * 16

    def _hash(self, key):
        return (hash(key) & 0x7fffffff) % self.m

    def put(self, key, val):
        if self.n > self.m / 2:
            self.keys = self.keys + [None] * self.m
            self.vals = self.vals + [None] * self.m
            self.m += self.m
        h = self._hash(key)
        while self.keys[h] is not None and self.keys[h] != key:
            h = (h + 1) % self.m
        self.keys[h] = key
        self.vals[h] = val
        self.n += 1

    def get(self, key):
        h = self._hash(key)
        init = h
        while True:
            if self.keys[h] is None:
                return None
            if self.keys[h] == key:
                return self.vals[h]
            h = (h + 1) % self.m
            if h == init:
                return None

st = LinearProbingHashST()
for i in range(2000):
    st.put(i, str(i))

for i in range(2000):
    print(st.get(i))