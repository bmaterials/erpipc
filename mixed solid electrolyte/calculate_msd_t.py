from initiating_structure import Ion_state
from initiating_structure import initial_stru

import numpy as np
from calculate_distance import calculate_distance

from get_allcor_deltatime import process_tao_dis, combine_data

import datetime


###离子跑100步
def calculate_parameters(ion_all_cor, tao_i_n_1):
    ## ion_all_cor存放的是10个离子跳跃过程中所有的坐标
    ## tao_i_n_1 = np.array(tao_i_n)  tao_i_n存放的是一种骨架结构情况下10个离子跳跃jump_num次 的时间间隔
    ### 先设定每个离子产生10个跃迁样本
    ### 分别取不同的步长来求 MSD/t,暂定步长分别为2，4，6，8，10

    D_ion_10 = []  ## 用来存放10个离子的扩散系数
    MSD_t_2 = []
    ##20步
    print('\n')
    print('2:')
    for j in range(0, 10):  ##
        # print('\n')
        # print('第' + str(j) + '个离子：')
        delta_r = []
        delta_t = []
        msd_t_1 = []
        for i in range(len(ion_all_cor) - 2000):
            delta_r_i = calculate_distance(ion_all_cor[i][j], ion_all_cor[i + 2000][j])
            delta_r.append(delta_r_i)  ### delta_r存放的是每个离子每个20步长的距离
        print('')
        for i in range(len(tao_i_n_1) - 1999):
            delta_t_i = sum(tao_i_n_1[i:i + 2000, j])
            delta_t.append(delta_t_i)  ### delta_t存放的是每个离子每2个步长的时间

        for i in range(len(delta_r)):
            msd_t_i = float(((delta_r[i]) ** 2) / delta_t[i])
            msd_t_1.append(msd_t_i)  ### 一个离子的9个小msd/t
        # print('2的小msd', msd_t_1, len(msd_t_1))  ##  msd_t_1求的是每个离子共跳10步 每两步长 求出的9个小msd/t
        msd_t_2 = float(sum(msd_t_1) / len(msd_t_1))  ###  msd_t_2 求的是9个小msd/t 的平均数
        MSD_t_2.append(msd_t_2)

    print('MSD_t_2')
    print(MSD_t_2)  ###  MSD_t_2 一维列表存放的是10个离子 2步长的 msd/t

    MSD_t_4 = []
    ## 4万步
    print('\n')
    print('4:')
    for j in range(0, 10):
        delta_r = []
        delta_t = []
        msd_t_1 = []
        for i in range(len(ion_all_cor) - 4000):
            delta_r_i = calculate_distance(ion_all_cor[i][j], ion_all_cor[i + 4000][j])
            delta_r.append(delta_r_i)  ### delta_r存放的是每个离子每4个步长的距离

        for i in range(len(tao_i_n_1) - 3999):
            delta_t_i = sum(tao_i_n_1[i:i + 4000, j])
            delta_t.append(delta_t_i)  ### delta_t存放的是每个离子每4个步长的时间

        for i in range(len(delta_r)):
            msd_t_i = float(((delta_r[i]) ** 2) / delta_t[i])
            msd_t_1.append(msd_t_i)
        # print('4的小msd', msd_t_1, len(msd_t_1))
        msd_t_4 = float(sum(msd_t_1) / len(msd_t_1))
        MSD_t_4.append(msd_t_4)

    print('MSD_t_4')
    print(MSD_t_4)

    MSD_t_6 = []
    ## 6万步
    print('\n')
    print('6:')
    for j in range(0, 10):
        # print('\n')
        # print('第' + str(j) + '个离子：')
        delta_r = []
        delta_t = []
        msd_t_1 = []
        for i in range(len(ion_all_cor) - 6000):
            delta_r_i = calculate_distance(ion_all_cor[i][j], ion_all_cor[i + 6000][j])
            delta_r.append(delta_r_i)  ### delta_r存放的是每个离子每6个步长的距离

        for i in range(len(tao_i_n_1) - 5999):
            delta_t_i = sum(tao_i_n_1[i:i + 6000, j])
            delta_t.append(delta_t_i)  ### delta_t存放的是每个离子每6个步长的时间

        for i in range(len(delta_r)):
            msd_t_i = float(((delta_r[i]) ** 2) / delta_t[i])
            msd_t_1.append(msd_t_i)
            # print(msd_t_i)
        # print('6的小msd', msd_t_1,len(msd_t_1))
        msd_t_6 = float(sum(msd_t_1) / len(msd_t_1))
        MSD_t_6.append(msd_t_6)

    print('MSD_t_6')
    print(MSD_t_6)

    MSD_t_8 = []
    ## 8万步
    print('\n')
    print('8:')
    for j in range(0, 10):
        # print('\n')
        # print('第' + str(j) + '个离子：')
        delta_r = []
        delta_t = []
        msd_t_1 = []
        for i in range(len(ion_all_cor) - 8000):
            delta_r_i = calculate_distance(ion_all_cor[i][j], ion_all_cor[i + 8000][j])
            delta_r.append(delta_r_i)  ### delta_r存放的是每个离子每8个步长的距离

        for i in range(len(tao_i_n_1) - 7999):
            delta_t_i = sum(tao_i_n_1[i:i + 8000, j])
            delta_t.append(delta_t_i)  ### delta_t存放的是每个离子每8个步长的时间

        for i in range(len(delta_r)):
            msd_t_i = float(((delta_r[i]) ** 2) / delta_t[i])
            msd_t_1.append(msd_t_i)

        # print('8的小msd', msd_t_1, len(msd_t_1))
        msd_t_8 = float(sum(msd_t_1) / len(msd_t_1))
        MSD_t_8.append(msd_t_8)

    print('MSD_t_8')
    print(MSD_t_8)

    ## 100 步
    MSD_t_10 = []
    print('\n')
    print('10:')
    for j in range(0, 10):
        # print('\n')
        # print('第' + str(j) + '个离子：')
        delta_r = calculate_distance(ion_all_cor[0][j], ion_all_cor[10][j])
        delta_t = sum(tao_i_n_1[:, j])
        msd_t = float(((delta_r ** 2) / delta_t))
        MSD_t_10.append(msd_t)
        # print('10的小msd', msd_t)
    print('MSD_t_10')
    print(MSD_t_10)
    #     for i in range(len(ion_all_cor) - 100):
    #         delta_r_i = calculate_distance(ion_all_cor[i][j], ion_all_cor[i + 100][j])
    #         delta_r.append(delta_r_i)  ### delta_r存放的是每个离子每10个步长的距离
    #     for i in range(len(tao_i_n_1) - 99):
    #         delta_t_i = sum(tao_i_n_1[i:i + 100, j])
    #         delta_t.append(delta_t_i)  ### delta_t存放的是每个离子每10个步长的时间
    #     for i in range(len(delta_r)):
    #         msd_t_i = float(((delta_r[i]) ** 2) / delta_t[i])
    #         msd_t_1.append(msd_t_i)
    #         msd_t_2 = float(sum(msd_t_1) / len(msd_t_1))
    #         MSD_t_10.append(msd_t_2)


    MSD_T_all = np.array([MSD_t_2, MSD_t_4, MSD_t_6, MSD_t_8, MSD_t_10])


    ###  接下来求 一种框架结构下 10个离子的扩散系数
    ###   MSD_T_all是4*10的列表  求每一列的平均数
    # MSD_T_all_1 = np.array(MSD_T_all)
    MSD_T_10_ion = MSD_T_all.mean(axis=0)  ##对 列求平均 得到 一种框架架构下 10 个离子的msd/t 存放在一个列表中

    for i in MSD_T_10_ion:
        D_ion_10.append(i / 6)
    print('10个离子的扩散系数分别是：')
    print(D_ion_10)

    D_total = float(sum(D_ion_10) / len(D_ion_10))
    print('一个体系总的扩散系数D_total:')
    print(D_total)

    return (D_total)


if __name__ == '__main__':

    time1 = datetime.datetime.now()
    print(time1)
    Ion_infor_all = []
    Ion_infor = []
    N = 7
    P = 0.9
    n0 = 0
    X = Y = Z = N
    Ion_num = 10
    jump_num = 10000
    tao_a = 2
    tao_b = 20000
    tao_c = 5000
    rate_hopping_a = 1 / tao_a
    rate_hopping_b = 1 / tao_b
    rate_hopping_c = 1 / tao_c
    D = []
    for i in range(1, 2):
        print('\n')
        print('第' + str(i) + '个骨架结构')
        a = initial_stru(P, X, Y, Z)
        print('a:')
        b = Ion_state(X, Y, Z, Ion_num)
        print('b:')
        i = process_tao_dis(a, b, jump_num, P, X, Y, Z, rate_hopping_a, rate_hopping_b, rate_hopping_c, N)
        print('c:')
        # xxx = np.array(i[1])
        j = calculate_parameters(i[0], i[1])
        # D.append(j)
        # print(D)

    time2 = datetime.datetime.now()
    print(time2)
    print(time2 - time1)




