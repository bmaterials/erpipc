# import scipy.io as sio
import numpy as np
# import os
import random
import datetime
#### 模块功能：根据设定的骨架结构尺寸（由参数N决定），搭建由聚合物和无机掺杂物构成的的初始结构；在骨架中随机洒Ion_num个Li+（记录所有离子的初始坐标）。

#
# class Site:
#     def __init__(self,cor):  #坐标、位点编号、邻居关系、什么是否占据、离子编号
#         self.cor = cor
#
#
# class Ion:
#     def __init__(self,Ion_num,cor_start,cor_end,t):
#         ##可存放离子位点的坐标，离子的编号，位点是否被存在离子，离子编号，
#         self.Ion_num = Ion_num
#         self.cor_start = cor_start
#         self.cor_end = cor_end
#         self.t = t

### shuffle 函数测试
"""import random

a = []
b = []
for i in range(100):
    a.append(i)

print(a)
print('样本平均：', float(sum(a)/len(a)))
pjz1 = []
for j in range(100):

    random.shuffle(a)
    # print(a)
    b = a[0:10]
    pjz = float(sum(b)/len(b))
    pjz1.append(pjz)

print('每次抽样的平均值：',pjz1)
print('最后总的平均值：', float(sum(pjz1)/len(pjz1)))
"""

def initial_stru(P,X,Y,Z ):  ##随机掺杂颗粒（这里指LLZO随机占据矩阵中的小方块）
    #返回位点的信息（坐标，编号，是否被占据等）

    x, y, z = np.mgrid[0:(2*X+1):2, 0:(2*Y+1):2, 0:(2*Z+1):2]
    site_coordinate = np.c_[x.ravel(), y.ravel(), z.ravel()]
    # print('所有位点（LLZO可存在的坐标）', len(site_coordinate))
    # print(site_coordinate)

    np.random.shuffle(site_coordinate)
    # random.shuffle(site_coordinate)  #打乱位点
    occupied_list = site_coordinate[0:int(P * X * Y * Z)]  #随机生成LLZO位点，并将对应的位点坐标存入列表中
    # return site_coordinate
    return occupied_list


def Ion_state(X,Y,Z,Ion_num):###离子随机占据格点,Ion_num表示填充的离子个数，将其设为变量
    ###返回的是一个包含十个离子坐标的列表

    x, y, z = np.mgrid[1:(2*X):2, 1:(2*Y):2, 1:(2*Z):2]
    ion_coordinate = np.c_[x.ravel(), y.ravel(), z.ravel()]
    # print('离子可在的坐标：总共有',len(ion_coordinate))
    # print(ion_coordinate)
    np.random.shuffle(ion_coordinate)
    # for i in range(0,10):
    #     occupied_ion.append(ion_list[i])  ####存放10个离子的坐标
    occupied_ion = ion_coordinate[0:Ion_num]
    # print('填充的离子坐标：',len(occupied_ion))
    # print(occupied_ion)

    return occupied_ion



if __name__ == '__main__':
    time1 = datetime.datetime.now()
    Ion_infor_all = []
    Ion_infor = []
    n0 = 0
    X = Y = Z = 5
    P = 0.2
    Ion_num = 10

    a = initial_stru(P,X,Y,Z)
    b = Ion_state(X,Y,Z,Ion_num)
    print('LLZO占据的位点坐标：',a)
    print('离子的初始坐标：',b)
    time2 = datetime.datetime.now()
    print(time2 - time1)
    ### 运行时间0:00:00.002992 和列表差不多



