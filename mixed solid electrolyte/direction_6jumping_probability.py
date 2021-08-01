
from initiating_structure import Ion_state
from initiating_structure import initial_stru
import random
from surrounding_8site_cor import Ion_sitneig
from surrounding_6_dope import Ion_surrounding
import datetime


def Ion_surrounding_tao(w_zhanju,rate_hopping_a,rate_hopping_b,rate_hopping_c):  ###w_zhanju  是Ion_surrounding的返回值  10组包含对离子周围掺杂物占据的判断
    #w1_10 = Ion_surrounding(P,X,Y,Z)
    tao_10 = []
    for w1 in w_zhanju:
        tao = []
        for i in range(len(w1)):
            #print(len(w1))
            if w1[i] == 0:
                tao.append(rate_hopping_c)  ##tao_a,tao_b,tao_c分别表示A,B,C键的步长
            elif w1[i] == 4:
                tao.append(rate_hopping_b)
            else:
                tao.append(rate_hopping_a)

        tao_10.append(tao)

        # tao =[]

    return tao_10


if __name__ == '__main__':

    time1 = datetime.datetime.now()
    Ion_infor_all = []
    Ion_infor = []
    N = 5
    P = 0.2
    n0 = 0
    X = Y = Z = N
    Ion_num = 10
    tao_a = 2
    tao_b = 20000
    tao_c = 5000
    rate_hopping_a = 1/tao_a
    rate_hopping_b = 1/tao_b
    rate_hopping_c = 1/tao_c
    a = initial_stru(P, X, Y, Z)
    b = Ion_state(X, Y, Z, Ion_num)
    c = Ion_sitneig(b)
    d = Ion_surrounding(a, c)
    #####site_cor用来存放掺杂物所占据的位点坐标,cor2_total存放的是Ion_sitneig的返回值，即10组列表，每组包含离子周围的位点坐标
    ##
    e = Ion_surrounding_tao(d, rate_hopping_a, rate_hopping_b,rate_hopping_c)  ###w_zhanju  是Ion_surrounding的返回值  10组包含对离子周围掺杂物占据的判断

    # print('无机纳米掺杂颗粒占据的位点坐标：', a)
    # print('离子的初始坐标：', b)
    # print('所有离子周围8个位点坐标：', c)
    # print('每个离子周围掺杂物占据的情况：', d)
    print('每个离子6个方向的跳跃概率：',e)

    time2 = datetime.datetime.now()
    print(time2 - time1)



