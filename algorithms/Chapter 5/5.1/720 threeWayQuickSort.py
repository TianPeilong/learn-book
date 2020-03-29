def charAt(s, d):
    return -1 if d >= len(s) else ord(s[d])

def sort(strings, lo, hi, d):
    if lo >= hi:
        return
    start = lo
    end = hi
    cur = lo + 1
    while cur <= end:
        if charAt(strings[cur], d) < charAt(strings[start], d):
            strings[cur], strings[start] = strings[start], strings[cur]
            start += 1
            cur += 1
        elif charAt(strings[start], d) < charAt(strings[cur], d):
            strings[cur], strings[end] = strings[end], strings[cur]
            end -= 1
        else:
            cur += 1
    sort(strings, lo, start - 1, d)
    if charAt(strings[start], d) >= 0:
        sort(strings, start, end, d + 1)
    sort(strings, end + 1, hi, d)
    

def threeWayQuickSort(strings):
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

threeWayQuickSort(strings)

for s in strings:
    print(s)