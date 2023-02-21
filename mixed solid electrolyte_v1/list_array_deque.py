import random
import numpy as np
import time
import sys
import matplotlib.pyplot as plt
from collections import deque

start = time.time()
length = []

list_size = []
array_size = []
deque_size = []

list_time = []
array_time = []
deque_time = []

for l in range(5, 1000, 5):
    print(l)
    length.append(l)
    a = [1] * l
    b = np.array(a)
    c = deque(maxlen=l)  ### 固定队列大小
    for i in range(l):
        c.append(1)

    ### a,b,c 长度都是295
# print('a:',len(a))
# print(a)
# print('b:',len(b))
# print(b)
# print('c:',len(c))
# print(c)



    print('list的size为：{}'.format(sys.getsizeof(a)))
    print('array的size为：{}'.format(sys.getsizeof(b)))
    print('deque的size为：{}'.format(sys.getsizeof(c)))
    list_size.append(sys.getsizeof(a))
    array_size.append(sys.getsizeof(b))
    deque_size.append(sys.getsizeof(c))

    for i in range(3):
        if i == 0:
            tmp = a
            name = 'list'
        elif i == 1:
            tmp = b
            name = 'array'
        else:
            tmp = c
            name = 'deque'

        s = time.time()
        for j in range(1000000):
            x = tmp[random.randint(0, len(a)-1)]
        duration = time.time() - s

        if name == 'list':
            list_time.append(duration)
        elif name == 'array':
            array_time.append(duration)
        else:
            deque_time.append(duration)

duration = time.time() - start
time_list = [0, 0, 0]
time_list[0] = duration // 3600
time_list[1] = (duration % 3600) // 60
time_list[2] = round(duration % 60, 2)
print('用时：' + str(time_list[0]) + ' 时 ' + str(time_list[1]) + '分' + str(time_list[2]) + '秒')

fig = plt.figure()

# ax1 = fig.add_subplot(211)
# ax1.plot(length, list_size, label='list')
# ax1.plot(length, array_size, label='array')
# ax1.plot(length, deque_size, label='deque')
# plt.xlabel('length')
# plt.ylabel('size')
# plt.legend()

ax2 = fig.add_subplot(212)
ax2.plot(length, list_time, label='list')
ax2.plot(length, array_time, label='array')
ax2.plot(length, deque_time, label='deque')
plt.xlabel('length')
plt.ylabel('time')
plt.legend()

plt.show()



####  数组元素比较
# import numpy as np
#
# a = [[4,6,18],[4,6,20],[4,8,18],[4,8,20],[6,6,18],[6,6,20],[6,8,18],[6,8,20]]
# b = [[4,6,18],[4,6,20],[4,8,18],[5,3,8],[7,7,9],[6,8,20],[3,3,3],[5,7,9],[2,5,1],[2,4,2],[8,5,5]]
#
# c = np.array(a)
# d = np.array(b)
#
# for i in c:
#     for j in d:
#         if (i==j).all():
#             print(i)
