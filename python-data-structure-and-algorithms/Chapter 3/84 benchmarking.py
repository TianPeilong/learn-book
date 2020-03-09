def nest(n):
    for x in range(n):
        for y in range(n):
            x + y

import timeit
def test2(n):
    ls = []
    for n in range(n):
        t = timeit.timeit('nest(' + str(n) + ')', setup='from __main__ import nest', number=1)
        ls.append(t)
    return ls

import matplotlib.pyplot as plt
n = 1000
plt.plot(test2(n))
plt.plot([x*x/10000000 for x in range(n)])
print('Benchmarking Finished!')
plt.show() # to show plot