
from initiating_structure import Ion_state as Ion_state
from initiating_structure import initial_stru as initial_stru
import random
from surrounding_8site_cor import Ion_sitneig
import numpy as np
import datetime

### surrounding_6_dope.py
###将函数形参改成坐标形式输入
def Ion_surrounding(site_cor,cor2_total):  #####site_cor用来存放掺杂物所占据的位点坐标,cor2_total存放的是Ion_sitneig的返回值，即10组列表，每组包含离子周围的位点坐标
    ###函数功能是判断离子周围6个方向分别有几个被掺杂物(llzo)占据的小方块


    #cor2_total = []  ###cor2_total存放的是Ion_sitneig的返回值，即10组列表，每组包含离子周围的位点坐标

    # for i in frame_cor:
    #     site_cor.append(i.cor)

    w_10 = []  ##存放10组w数据，一组w里面存放的是一个离子周围6个方向分别有的掺杂小方块个数

    for cor_i_total in cor2_total:  ##遍历10离子坐标
        ###前面
        # print(cor_i_total)
        # print('前：')

        # for i in c:
        #     for j in d:
        #         if (i == j).all():
        #             print(i)

        w_front = 0
        # w = []
        for i in cor_i_total[4:8]:
            for j in site_cor[:]:
                if (i == j).all():
                    # print(i)
                    w_front += 1


        ##后方
        # print('后')
        w_behind = 0
        for i in cor_i_total[0:4]:
            for j in site_cor[:]:
                if (i == j).all():
                    # print(i)
                    w_behind += 1


        ###上方
        # print('上')
        w_up = 0
        for i in range(1, 8, 2):
            for j in site_cor[:]:
                if (cor_i_total[i] == j).all():
                    # print(cor_i_total[i])
                    w_up += 1

        ##下方
        # print('下')
        w_down = 0
        for i in range(0, 8, 2):
            for j in site_cor[:]:
                if (cor_i_total[i] == j).all():
                    # print(cor_i_total[i])
                    w_down += 1

        ##左方
        # print('左')
        w_left1 = 0
        w_left2 = 0
        for i in range(0, 2):
            for j in site_cor[:]:
                if (cor_i_total[i] == j).all():
                    # print(cor_i_total[i])
                    w_left1 += 1
                    # print('左边2个小方块中被llzo占据的坐标：')
                    # print(j)
        for i in range(4, 6):
            for j in site_cor[:]:
                if (cor_i_total[i] == j).all():
                    # print(cor_i_total[i])
                    w_left2 += 1
                    # print('左边2个小方块中被llzo占据的坐标：')
                    # print(j)
        w_left = w_left1 + w_left2
        # print('w_left = ')
        # print(w_left)

        ##右方
        # print('右')
        w_right1 = 0
        w_right2 = 0
        for i in range(2, 4):
            for j in site_cor[:]:
                if (cor_i_total[i] == j).all():
                    # print(cor_i_total[i])
                    w_right1 += 1

        for i in range(6, 8):
            for j in site_cor[:]:
                if (cor_i_total[i] == j).all():
                    # print(cor_i_total[i])
                    w_right2 += 1
                    # print('右边2个小方块中被llzo占据的坐标：')
                    # print(j)
        w_right = w_right1 + w_right2
        # print('w_right = ')
        # print(w_right)

        w = [w_front,w_behind,w_up,w_down,w_left,w_right]
        w_10.append(w)
        # w = []


    # print('前后上下左右被占据的个数分别为：')
    # print(w_10)

    return w_10

if __name__ == '__main__':

    time1 = datetime.datetime.now()
    Ion_infor_all = []
    Ion_infor = []
    n0 = 0
    N = 5
    P = 0.2
    X = Y = Z = N
    Ion_num = 10
    a = initial_stru(P, X, Y, Z)
    b = Ion_state(X, Y, Z, Ion_num)
    c = Ion_sitneig(b)
    d = Ion_surrounding(a, c)
    #####site_cor用来存放掺杂物所占据的位点坐标,cor2_total存放的是Ion_sitneig的返回值，即10组列表，每组包含离子周围的位点坐标
    ##

    # print('无机纳米掺杂颗粒占据的位点坐标：', a)
    # print('离子的初始坐标：', b)
    # print('所有离子周围8个位点坐标：', c)
    print('每个离子周围掺杂物占据的情况：', d)

    time2 = datetime.datetime.now()
    print(time2 - time1)

