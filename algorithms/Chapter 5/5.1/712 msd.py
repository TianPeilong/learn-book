def sort(strings, lo, hi, pos):
    if lo > hi:
        return
    R = 256 + 2
    counter = [0] * R
    subStrings = strings[lo:hi+1]
    aux = [''] * (hi-lo+1)
    for s in subStrings:
        if pos >= len(s):
            counter[1] += 1
        else:
            counter[ord(s[pos]) + 2] += 1
    for i in range(1, R):
        counter[i] += counter[i-1]
    for s in subStrings:
        if pos >= len(s):
            aux[counter[0]] = s
            counter[0] += 1
        else:
            aux[counter[ord(s[pos])+1]] = s
            counter[ord(s[pos])+1] += 1
    strings[lo:hi+1] = aux[:]
    start = counter[0]
    npos = pos + 1
    for count in counter:
        if count > start:
            sort(strings, lo+start, lo + count - 1, npos)
            start = count

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