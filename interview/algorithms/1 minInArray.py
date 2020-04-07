'''
给一个数组，定义X为某个区间的最小值乘上这个区间内所有元素的和，求最大的X。如数组为3 1 6 4 5，则最大的X=4*（6+4+5）=60
https://blog.csdn.net/u013616945/article/details/77508372
'''

def minArr(arr):
    if not arr:
        return 0
    if len(arr) == 1:
        return arr[0] ** 2
    stack = [0]
    maxV = arr[0] ** 2
    for i in range(1, len(arr)):
        if arr[i] >= arr[stack[-1]]:
            stack.append(i)
        else:
            while stack and arr[stack[-1]] > arr[i]:
                cur = stack.pop()
                left = -1
                if stack:
                    left = stack[-1]
                curV = sum(arr[left+1:i]) * arr[cur]
                maxV = max(maxV, curV)
            stack.append(i)
    right = len(arr)
    while stack:
        cur = stack.pop()
        left = -1
        if stack:
            left = stack[-1]
        curV = sum(arr[left+1:right]) * arr[cur]
        maxV = max(maxV, curV)  
    return maxV

print(minArr([3,1,6,4,5]))
