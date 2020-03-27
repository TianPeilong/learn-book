def sort(strings, lo, hi, pos):
    r = 256 + 2
    aux = [''] * (hi - lo + 1)
    cache = [0] * r
    sort_strs = strings[lo:hi+1]
    for s in sort_strs:
        if pos >= len(s):
            cache[1] += 1
        else:
            cache[ord(s[pos])+2] += 1
    for j in range(1, r):
        cache[j] += cache[j-1]
    for s in sort_strs:
        if pos >= len(s):
            aux[cache[0]] = s
            cache[0] += 1
        else:
            aux[cache[ord(s[pos])+1]] = s
            cache[ord(s[pos])+1] += 1
    strings[lo:hi+1] = aux[:]
    start = lo + cache[1]
    pos += 1
    for count in cache[1:]:
        if count > start:
            sort(strings, start, lo + count -1, pos)
            start = lo + count

def msd(strings):
    sort(strings, 0, len(strings)-1, 0)

strings = [
    'she',
    'sells',
    'seashells',
    'by',
    'the',
    'sea',
    'shore',
    'the',
    'shells',
    'she',
    'sells',
    'are',
    'surely',
    'seashells'
]

msd(strings)

for s in strings:
    print(s)