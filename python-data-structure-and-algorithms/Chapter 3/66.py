def bitStr(n, s):
    if n == 1: return s
    return [ dight + bits for dight in bitStr(1, s) for bits in bitStr(n-1, s)]
print(bitStr(3, 'abc'))