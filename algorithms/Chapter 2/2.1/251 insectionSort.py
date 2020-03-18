def insertion_sort(l):
    def insert_before(l, target, source):
        l[target:source+1] = [l[source]] + l[target:source]

    for i in range(1, len(l)):
        pos = i
        for j in range(i-1,-1,-1):
            if l[i] < l[j]:
                pos = j
            else:
                break
        insert_before(l, pos, i)

# book
def insertion_sort_book(l):
    def exchange(l, i, j):
        temp = l[i]
        l[i] = l[j]
        l[j] = temp
    for i in range(1, len(l)):
        for j in range(i, 0, -1):
            if l[j] < l[j-1]:
                exchange(l, j, j-1)
        
case = [4,3,5,6,78,8]
insertion_sort_book(case)
print(case)