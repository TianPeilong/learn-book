import sys
import os

print('当前 Python 解释器路径：')
print(sys.executable)

print()
print('当前 Python 解释器目录：')
print(os.path.dirname(sys.executable))

a = 0
b = 0.0
l = []
none_list = [None, False, 0, a, 0.0, l]
for n in none_list:
    if n:
        print(str(n) + ' is True')
    else:
        print(str(n) + ' is False')

print(1-0.9-0.1==0)

case = 'ABC' < 'A'
print(case)