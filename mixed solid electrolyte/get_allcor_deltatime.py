
from initiating_structure import Ion_state
from initiating_structure import initial_stru
import random
from surrounding_8site_cor import Ion_sitneig
from surrounding_6_dope import Ion_surrounding
from direction_6jumping_probability import Ion_surrounding_tao
import numpy as np
from new_cor import Ion_choose
import datetime




def combine_data(site_infor, ion_infor, rate_hopping_a, rate_hopping_b, rate_hopping_c, N): ##掺杂物坐标，离子坐标,rh_a,rh_b,rh_c分别是跳跃率 ,N是骨架尺寸
    ### 函数功能：同时返回离子初始坐标，跳跃率，跳跃方向，更新后的坐标


    # print('离子每次跳跃前的坐标是：')
    # print(ion_infor)
    a1 = Ion_sitneig(ion_infor)   ###找出离子周围的位点坐标
    a2 = Ion_surrounding(site_infor,a1)  ##找出离子6个方向被掺杂物占据的位点的个数
    a3 = Ion_surrounding_tao(a2,rate_hopping_a,rate_hopping_b,rate_hopping_c) ####找出离子6个方向的跳跃概率
    a4 = Ion_choose(a3, ion_infor, N) ##找出每个离子具体跳跃率，跳跃方向
    ###Ion_choose(tao_all,ion_cor_10,N):###存放的是每个离子6个方向的tao,共10组/ion_cor_10是10个离子坐标
    ###返回ion_cor_10,np_tao,np_allcor
    # x = []   ###跳跃率
    # y = []   ###跳跃方向
    # z = [] ### 新坐标
    # for i in range(0, 10):
    #     x.append(a4[0][i])
    #     y.append(a4[1][i])
    # a5 = update_cor(y,ion_infor)  ###离子跳跃后新的坐标
    # a6 = []
    # a6.append(ion_infor)
    # a6.append(x)
    # a6.append(y)
    # a6.append(a5)
    return ion_infor,a4[1],a4[2]  ## 得到所有离子的初始离子坐标，跳跃概率，更新后的坐标
    # return a6  ###  得到所有离子的初始离子坐标，跳跃概率，跳跃方向，更新后的坐标

def process_tao_dis(a,occupied_ion,jump_num,P,X,Y,Z,rate_hopping_a,rate_hopping_b,rate_hopping_c,N):
    ### jump_num是离子跑的步数
    ## a是掺杂物坐标，occupied_ion是离子初始坐标

    ### 函数功能，返回离子跳跃过程中的时间间隔，坐标更新


    # tao_cor =[]
    bb = []
    tao_i_n = []

    for j in range(0, jump_num):

        if j == 0:
            ww = combine_data(a, occupied_ion, rate_hopping_a, rate_hopping_b, rate_hopping_c, N)
    ##得到所有离子的初始离子坐标，跳跃概率，更新后的坐标
        else:
            ww = combine_data(a, ss, rate_hopping_a, rate_hopping_b, rate_hopping_c, N)

        ss = ww[2]  ##传入新的离子坐标

        ###  ww[0]存放的是每次跳跃10个离子的初始坐标，ww[1]存放的是每次跳跃10个离子的跳跃率，
        ###  ww[2]存放的是每次跳跃10个离子更新的坐标


        # aa.append(ww[0])  ###存放jump_num组10个离子的旧坐标
        bb.append(ww[2])  ###存放jump_num组10个离子的新坐标

        tao_i = []

        for i in ww[1]:
            tao_i.append(1 / i)
        # print('每次跳跃时长：')
        # print(tao_i)
        tao_i_n.append(tao_i)  ### tao_i_n存放的是 ump_num组10个离子的跳跃时间间隔

    tao_i1 = np.array(tao_i_n)


    bb.insert(0, occupied_ion)  ###此时bb存放的是10个离子从初始态到末态所有的坐标
    cc = np.array(bb)
    # print('离子跃迁过程中的所有坐标：', cc)
    # tao_cor.append(cc)
    # tao_cor.append(tao_i1)

    return cc,tao_i1  ### cc 是离子跳跃过程的所有坐标/tao_i1是跳跃过程中的时间间隔

if __name__ == '__main__':
    time1 = datetime.datetime.now()
    Ion_infor_all = []
    Ion_infor = []
    N = 5
    n0 = 0
    X = Y = Z = N
    P = 0.01
    Ion_num = 10
    jump_num = 100
    tao_a = 2
    tao_b = 20000
    tao_c = 5000
    rate_hopping_a = 1 / tao_a
    rate_hopping_b = 1 / tao_b
    rate_hopping_c = 1 / tao_c

    a = initial_stru(P, X, Y, Z)
    b = Ion_state(X, Y, Z, Ion_num)
    c = Ion_sitneig(b)
    d = Ion_surrounding(a, c)
    #####site_cor用来存放掺杂物所占据的位点坐标,cor2_total存放的是Ion_sitneig的返回值，即10组列表，每组包含离子周围的位点坐标
    ##
    e = Ion_surrounding_tao(d, rate_hopping_a, rate_hopping_b,
                            rate_hopping_c)  ###w_zhanju  是Ion_surrounding的返回值  10组包含对离子周围掺杂物占据的判断
    f = Ion_choose(e, b, N)  ###存放的是离子6个方向的tao,共10组/ion_cor_10是10个离子坐标
    ###turn存放的是每个离子所选择跳跃的方向,以列表的形式存放/ion_cor_10存放的是10组离子坐标
    g = combine_data(a, b, rate_hopping_a, rate_hopping_b, rate_hopping_c, N)
    ##掺杂物坐标，离子坐标,rh_a,rh_b,rh_c分别是跳跃率 ,N是骨架尺寸
    h = process_tao_dis(a,b,jump_num,P,X,Y,Z,rate_hopping_a,rate_hopping_b,rate_hopping_c,N)
    ### jump_num是离子跑的步数
    ## a是掺杂物坐标，occupied_ion是离子初始坐标

    # print('无机纳米掺杂颗粒占据的位点坐标：', a)
    # print('离子的初始坐标：', b)
    # print('所有离子周围8个位点坐标：', c)
    # print('每个离子周围掺杂物占据的情况：', d)
    # print('每个离子6个方向的跳跃概率：', e)
    # print('每个离子选择的跳跃方向及该方向对应的概率：', f)
    # print('离子迁移后新的坐标：', g)
    # print('离子更新后的信息：', h)  ## 跳跃前的坐标，跳跃概率，跳跃方向，跳跃后坐标
    print('记录离子跳跃过程中的坐标及时间步长：',h)
    # print(len(h[0]),len(h[1]))

    # print('离子所有跳跃：')
    # i = h[0]
    # for c in i:
    #     print(c)

    # print('第一个坐标：')
    # for h in range(len(i)):
    #     print(i[h][0],h)
    #
    # for j in range(len(i)):
    #     for k in range(j,len(i)):
    #         if (i[j][0] == i[k][0]).all():
    #             print('重复跳跃：')
    #             print(i[j][0],j)







    time2 = datetime.datetime.now()
    print(time2 - time1)
