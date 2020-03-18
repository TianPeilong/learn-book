def selection_sort(l):
    def exchange(l, i, j):
        temp = l[i]
        l[i] = l[j]
        l[j] = temp

    for i in range(len(l)):
        cur = i
        for j in range(i+1, len(l)):
            if l[j] < l[cur]:
                cur = j
        exchange(l, i, cur)

case = [4,3,5,6,78,8]
selection_sort(case)
print(case)