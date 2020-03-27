def lsd(strings, w):
    n = len(strings)
    r = 256 + 1
    aux = [''] * n
    for i in range(w-1,-1,-1):
        cache = [0] * r
        for s in strings:
            cache[ord(s[i]) + 1] += 1
        for j in range(1, r):
            cache[j] += cache[j-1]
        for s in strings:
            aux[cache[ord(s[i])]] = s
            cache[ord(s[i])] += 1
        strings[:] = aux[:]
    return strings

strings = [
    '4PGC938',
    '2IYE230',
    '3CIO720',
    '1ICK750',
    '1OHV845',
    '4JZY524',
    '1ICK750',
    '3CIO720',
    '1OHV845',
    '1OHV845',
    '2RLA629',
    '2RLA629',
    '3ATW723'
]

result = lsd(strings, 7)
for s in result:
    print(s)

        
