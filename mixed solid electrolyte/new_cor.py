
from initiating_structure import Ion_state as Ion_state
from initiating_structure import initial_stru as initial_stru
import random
from surrounding_8site_cor import Ion_sitneig
from surrounding_6_dope import Ion_surrounding
from direction_6jumping_probability import Ion_surrounding_tao
import datetime
import numpy as np


def Ion_choose(tao_all,ion_cor_10,N):###存放的是每个离子6个方向的tao,共10组/ion_cor_10是10个离子坐标
    ###确定每个离子所选的的跳跃率，以及选择上下前后左右哪个方向跳跃
    ###方向顺序 front、behind、up、down、left、right
    # print('离子跳跃方向：')
    # print(tao_all)
    choose_all = []
    turn_n_all = []
    choose_turn = []


    for i in range(0, len(tao_all)):  ###找出处在角、棱、面上的离子  这几个特殊离子
        # global turn_n
        # global choose_n

        ##测试N=5,  1~9
        #####方向顺序 front、behind、up、down、left、right##
        ## 角[1,1,1]
        ##1
        # corner_1 = []
        # corner_2 = []
        # corner_3 = []
        # corner_4 = []
        # corner_5 = []
        # corner_6 = []
        # corner_7 = []
        # corner_8 = []
        # arris_1 = []
        # arris_2 = []
        # arris_3 = []
        # arris_4 = []
        # arris_5 = []
        # arris_6 = []
        # arris_7 = []
        # arris_8 = []
        # arris_9 = []
        # arris_10 = []
        # arris_11 = []
        # arris_12 = []
        # surface_1 = []
        # surface_2 = []
        # surface_3 = []
        # surface_4 = []
        # surface_5 = []
        # surface_6 = []
        ran = random.uniform(0, 1)

        if ion_cor_10[i][0] == ion_cor_10[i][1] == ion_cor_10[i][2] == 1:
            # print('1，左后下角,前上右')
            # print('原坐标：',ion_cor_10[i])
            # corner_1.append(tao_all[i][0])  # front
            # corner_1.append(tao_all[i][2])  # up
            # corner_1.append(tao_all[i][5])  # right
            corner = [tao_all[i][0],tao_all[i][2],tao_all[i][5]]
            # print('所有概率：',tao_all[i])
            # print('可选概率：0 2 5',corner_1)

            sum1 = sum(corner)
            # ran1 = random.uniform(0, 1)
            s_r = sum1 * ran

            if 0 <= s_r < corner[0]:
                turn_n = 'front'
                choose_n = corner[0]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            elif corner[0] <= s_r < corner[0] + corner[1]:
                turn_n = 'up'
                choose_n = corner[1]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            elif corner[0] + corner[1] <= s_r < corner[0] + corner[1] + corner[2]:
                turn_n = 'right'
                choose_n = corner[2]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)

            # print('方向：', turn_n)
            turn_n_all.append(turn_n)
            choose_all.append(choose_n)

        #####方向顺序 front、behind、up、down、left、right
        ##2
        elif ion_cor_10[i][0] == (2*N-1) and ion_cor_10[i][1] == ion_cor_10[i][2] == 1:
            # print('2:前左下角，后上右')
            # print('原坐标：',ion_cor_10[i])
            # corner_2.append(tao_all[i][1])  # behind
            # corner_2.append(tao_all[i][2])  # up
            # corner_2.append(tao_all[i][5])  # right
            corner = [tao_all[i][1],tao_all[i][2],tao_all[i][5]]
            # print('所有概率：', tao_all[i])
            # print('可选概率：1 2 5', corner_2)

            sum1 = sum(corner)
            # ran2 = random.uniform(0, 1)
            s_r = sum1 * ran

            if 0 <= s_r < corner[0]:
                turn_n = 'behind'
                choose_n = corner[0]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)

            elif corner[0] <= s_r < corner[0] + corner[1]:
                turn_n = 'up'
                choose_n = corner[1]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            elif corner[0] + corner[1] <= s_r < corner[0] + corner[1] + corner[2]:
                turn_n = 'right'
                choose_n = corner[2]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)

            # print('方向：', turn_n)
            turn_n_all.append(turn_n)
            choose_all.append(choose_n)

        ##3
        #####方向顺序 front、behind、up、down、left、right
        elif ion_cor_10[i][0] == 1 and ion_cor_10[i][1] == (2*N-1) and ion_cor_10[i][2] == 1:
            # print('3:后右下，前上左')
            # print('原坐标：',ion_cor_10[i])
            # corner_3.append(tao_all[i][0])  # front
            # corner_3.append(tao_all[i][2])  # up
            # corner_3.append(tao_all[i][4])  # left
            corner = [tao_all[i][0],tao_all[i][2],tao_all[i][4]]
            # print('所有概率：', tao_all[i])
            # print('可选概率：0 2 4', corner_3)

            sum1 = sum(corner)
            # ran3 = random.uniform(0, 1)
            s_r = sum1 * ran

            if 0 <= s_r < corner[0]:
                turn_n = 'front'
                choose_n = corner[0]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)

            elif corner[0] <= s_r < corner[0] + corner[1]:
                turn_n = 'up'
                choose_n = corner[1]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            elif corner[0] + corner[1] <= s_r < corner[0] + corner[1] + corner[2]:
                turn_n = 'left'
                choose_n = corner[2]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            # print('方向：', turn_n)
            turn_n_all.append(turn_n)
            choose_all.append(choose_n)

        ##4
        #####方向顺序 front、behind、up、down、left、right
        elif ion_cor_10[i][0] == ion_cor_10[i][1] == (2*N-1) and ion_cor_10[i][2] == 1:
            # print('4:前右下，后上左')
            # print('原坐标：',ion_cor_10[i])
            # corner_4.append(tao_all[i][1])  # behind
            # corner_4.append(tao_all[i][2])  # up
            # corner_4.append(tao_all[i][4])  # left
            corner = [tao_all[i][1],tao_all[i][2],tao_all[i][4]]
            # print('所有概率：', tao_all[i])
            # print('可选概率：1 2 4', corner_4)

            sum1 = sum(corner)
            # ran4 = random.uniform(0, 1)
            s_r = sum1 * ran

            if 0 <= s_r < corner[0]:
                turn_n = 'behind'
                choose_n = corner[0]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            elif corner[0] <= s_r < corner[0] + corner[1]:
                turn_n = 'up'
                choose_n = corner[1]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            elif corner[0] + corner[1] <= s_r < corner[0] + corner[1] + corner[2]:
                turn_n = 'left'
                choose_n = corner[2]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            # print('方向：', turn_n)
            turn_n_all.append(turn_n)
            choose_all.append(choose_n)

        ##5
        #####方向顺序 front、behind、up、down、left、right
        elif ion_cor_10[i][0] == ion_cor_10[i][1] == 1 and ion_cor_10[i][2] == (2*N-1):
            # print('5:后左上角，前下右')
            # print('原坐标：',ion_cor_10[i])
            # corner_5.append(tao_all[i][0])  # front
            # corner_5.append(tao_all[i][3])  # down
            # corner_5.append(tao_all[i][5])  # right
            corner = [tao_all[i][0],tao_all[i][3],tao_all[i][5]]
            # print('所有概率：', tao_all[i])
            # print('可选概率：0 3 5', corner_5)

            sum1 = sum(corner)
            # ran5 = random.uniform(0, 1)
            s_r = sum1 * ran

            if 0 <= s_r < corner[0]:
                turn_n = 'front'
                choose_n = corner[0]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            elif corner[0] <= s_r < corner[0] + corner[1]:
                turn_n = 'down'
                choose_n = corner[1]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            elif corner[0] + corner[1] <= s_r < corner[0] + corner[1] + corner[2]:
                turn_n = 'right'
                choose_n = corner[2]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            # print('方向：', turn_n)
            turn_n_all.append(turn_n)
            choose_all.append(choose_n)

        ##6
        #####方向顺序 front、behind、up、down、left、right
        elif ion_cor_10[i][0] == (2*N-1) and ion_cor_10[i][1] == 1 and ion_cor_10[i][2] == (2*N-1):
            # print('6:前左上角，后下右')
            # print('原坐标：',ion_cor_10[i])
            # corner_6.append(tao_all[i][1])  # behind
            # corner_6.append(tao_all[i][3])  # down
            # corner_6.append(tao_all[i][5])  # right
            corner = [tao_all[i][1],tao_all[i][3],tao_all[i][5]]
            # print('所有概率：', tao_all[i])
            # print('可选概率：1 3 5', corner_6)

            sum1 = sum(corner)
            # ran = random.uniform(0, 1)
            s_r = sum1 * ran

            if 0 <= s_r < corner[0]:
                turn_n = 'behind'
                choose_n = corner[0]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            elif corner[0] <= s_r < corner[0] + corner[1]:
                turn_n = 'down'
                choose_n = corner[1]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            elif corner[0] + corner[1] <= s_r < corner[0] + corner[1] + corner[2]:
                turn_n = 'right'
                choose_n = corner[2]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            # print('方向：', turn_n)
            turn_n_all.append(turn_n)
            choose_all.append(choose_n)

        ##7
        #####方向顺序 front、behind、up、down、left、right
        elif ion_cor_10[i][0] == 1 and ion_cor_10[i][1] == ion_cor_10[i][2] == (2*N-1):
            # print('7:后右上，前下左')
            # print('原坐标：',ion_cor_10[i])
            # corner_7.append(tao_all[i][0])  # front
            # corner_7.append(tao_all[i][3])  # down
            # corner_7.append(tao_all[i][4])  # left
            corner = [tao_all[i][0],tao_all[i][3],tao_all[i][4]]
            # print('所有概率：', tao_all[i])
            # print('可选概率：0 3 4', corner_7)

            sum1 = sum(corner)
            # ran7 = random.uniform(0, 1)
            s_r = sum1 * ran

            if 0 <= s_r < corner[0]:
                turn_n = 'front'
                choose_n = corner[0]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            elif corner[0] <= s_r < corner[0] + corner[1]:
                turn_n = 'down'
                choose_n = corner[1]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            elif corner[0] + corner[1] <= s_r < corner[0] + corner[1] + corner[2]:
                turn_n = 'left'
                choose_n = corner[2]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            # print('方向：', turn_n)
            turn_n_all.append(turn_n)
            choose_all.append(choose_n)

        ##8
        #####方向顺序 front、behind、up、down、left、right
        elif ion_cor_10[i][0] == ion_cor_10[i][1] == ion_cor_10[i][2] == (2*N-1):
            # print('8:前右上，后下左')
            # print('原坐标：',ion_cor_10[i])
            # corner_8.append(tao_all[i][1])  # behind
            # corner_8.append(tao_all[i][3])  # down
            # corner_8.append(tao_all[i][4])  # left
            corner = [tao_all[i][1],tao_all[i][3],tao_all[i][4]]
            # print('所有概率：', tao_all[i])
            # print('可选概率：1 3 4', corner_8)

            sum1 = sum(corner)
            # ran8 = random.uniform(0, 1)
            s_r = sum1 * ran

            if 0 <= s_r < corner[0]:
                turn_n = 'behind'
                choose_n = corner[0]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            elif corner[0] <= s_r < corner[0] + corner[1]:
                turn_n = 'down'
                choose_n = corner[1]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            elif corner[0] + corner[1] <= s_r < corner[0] + corner[1] + corner[2]:
                turn_n = 'left'
                choose_n = corner[2]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            # print('方向：', turn_n)
            turn_n_all.append(turn_n)
            choose_all.append(choose_n)

        ##9
        #####方向顺序 front、behind、up、down、left、right
        elif  1 < ion_cor_10[i][0] <(2*N-1) and ion_cor_10[i][1] == ion_cor_10[i][2] == 1:
            # print('9:左下线,前后上右')
            # print('原坐标：',ion_cor_10[i])
            # arris_1.append(tao_all[i][0]) #front、behind、up、right
            # arris_1.append(tao_all[i][1])
            # arris_1.append(tao_all[i][2])
            corner = [tao_all[i][0],tao_all[i][1],tao_all[i][2]]
            # print('所有概率：', tao_all[i])
            # print('可选概率：0 1 2 5', arris_1)

            sum1 = sum(corner)
            # ran9 = random.uniform(0, 1)
            s_r = sum1 * ran

            if 0 <= s_r < corner[0]:
                turn_n = 'front'
                choose_n = corner[0]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            elif corner[0] <= s_r < corner[0] + corner[1]:
                turn_n = 'behind'
                choose_n = corner[1]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            elif corner[0] + corner[1] <= s_r < corner[0] + corner[1] + corner[2]:
                turn_n = 'up'
                choose_n = corner[2]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            elif corner[0] + corner[1] + corner[2] <= s_r < corner[0] + corner[1] + corner[2] + corner[3]:
                turn_n = 'right'
                choose_n = corner[3]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            # print('方向：', turn_n)
            turn_n_all.append(turn_n)
            choose_all.append(choose_n)

        ##10
        #####方向顺序 front、behind、up、down、left、right
        elif ion_cor_10[i][0] == (2*N-1) and 1 < ion_cor_10[i][1] < (2*N-1) and ion_cor_10[i][2] == 1:
            # print('10:前下线,后上左右')
            # print('原坐标：',ion_cor_10[i])
            # arris_2.append(tao_all[i][1]) #behind、up、left、right
            # arris_2.append(tao_all[i][2])
            # arris_2.append(tao_all[i][4])
            # arris_2.append(tao_all[i][5])
            corner = [tao_all[i][1],tao_all[i][2],tao_all[i][4],tao_all[i][5]]
            # print('所有概率：', tao_all[i])
            # print('可选概率：1 2 4 5', arris_2)

            sum1 = sum(corner)
            # ran10 = random.uniform(0, 1)
            s_r = sum1 * ran

            if 0 <= s_r < corner[0]:
                turn_n = 'behind'
                choose_n = corner[0]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)

            elif corner[0] <= s_r < corner[0] + corner[1]:
                turn_n = 'up'
                choose_n = corner[1]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)

            elif corner[0] + corner[1] <= s_r < corner[0] + corner[1] + corner[2]:
                turn_n = 'left'
                choose_n = corner[2]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)

            elif corner[0] + corner[1] + corner[2] <= s_r < corner[0] + corner[1] + corner[2] + corner[3]:
                turn_n = 'right'
                choose_n = corner[3]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            # print('方向：', turn_n)
            turn_n_all.append(turn_n)
            choose_all.append(choose_n)

        ##11
        #####方向顺序 front、behind、up、down、left、right
        elif  1 < ion_cor_10[i][0] < (2*N-1) and ion_cor_10[i][1] == (2*N-1) and ion_cor_10[i][2] == 1:
            # print('11:右下线,前后上左')
            # print('原坐标：',ion_cor_10[i])
            # arris_3.append(tao_all[i][0])
            # arris_3.append(tao_all[i][1])
            # arris_3.append(tao_all[i][2])
            # arris_3.append(tao_all[i][4])
            corner = [tao_all[i][0],tao_all[i][1],tao_all[i][2],tao_all[i][4]]
            # print('所有概率：', tao_all[i])
            # print('可选概率：0 1 2 4 ', arris_3)

            sum1 = sum(corner)
            # ran11 = random.uniform(0, 1)
            s_r = sum1 * ran

            if 0 <= s_r < corner[0]:
                turn_n = 'front'
                choose_n = corner[0]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)

            elif corner[0] <= s_r < corner[0] + corner[1]:
                turn_n = 'behind'
                choose_n = corner[1]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)

            elif corner[0] + corner[1] <= s_r < corner[0] + corner[1] + corner[2]:
                turn_n = 'up'
                choose_n = corner[2]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)

            elif corner[0] + corner[1] + corner[2] <= s_r < corner[0] + corner[1] + corner[2] + corner[3]:
                turn_n = 'left'
                choose_n = corner[3]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            # print('方向：', turn_n)
            turn_n_all.append(turn_n)
            choose_all.append(choose_n)

        ## 12
        #####方向顺序 front、behind、up、down、left、right
        elif ion_cor_10[i][0] == ion_cor_10[i][2] == 1 and 1 < ion_cor_10[i][1] < (2*N-1):
            # print('12:后下线,前上左右')
            # print('原坐标：',ion_cor_10[i])
            # arris_4.append(tao_all[i][0])  # front、up、left、right
            # arris_4.append(tao_all[i][2])
            # arris_4.append(tao_all[i][4])
            # arris_4.append(tao_all[i][5])
            corner = [tao_all[i][0],tao_all[i][2],tao_all[i][4],tao_all[i][5]]
            # print('所有概率：', tao_all[i])
            # print('可选概率：0 2 4 5 ', arris_4)

            sum1 = sum(corner)
            # ran12 = random.uniform(0, 1)
            s_r = sum1 * ran

            if 0 <= s_r < corner[0]:
                turn_n = 'front'
                choose_n = corner[0]

                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            elif corner[0] <= s_r < corner[0] + corner[1]:
                turn_n = 'up'
                choose_n = corner[1]

                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            elif corner[0] + corner[1] <= s_r < corner[0] + corner[1] + corner[2]:
                turn_n = 'left'
                choose_n = corner[2]

                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            elif corner[0] + corner[1] + corner[2] <= s_r < corner[0] + corner[1] + corner[2] + corner[3]:
                turn_n = 'right'
                choose_n = corner[3]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            # print('方向：', turn_n)
            turn_n_all.append(turn_n)
            choose_all.append(choose_n)

        ## 13
        #####方向顺序 front、behind、up、down、left、right
        elif ion_cor_10[i][0] == ion_cor_10[i][1] == 1 and 1 < ion_cor_10[i][2] < (2*N-1):
            # print('13:左后线，')
            # print('原坐标：',ion_cor_10[i])
            # arris_5.append(tao_all[i][0])  # front、up、down、right
            # arris_5.append(tao_all[i][2])
            # arris_5.append(tao_all[i][3])
            # arris_5.append(tao_all[i][5])
            corner = [tao_all[i][0], tao_all[i][2], tao_all[i][3], tao_all[i][5]]
            # print('所有概率：', tao_all[i])
            # print('可选概率：0 2 3 5 ', arris_5)

            sum1 = sum(corner)
            # ran13 = random.uniform(0, 1)
            s_r = sum1 * ran

            if 0 <= s_r < corner[0]:
                turn_n = 'front'
                choose_n = corner[0]

                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            elif corner[0] <= s_r < corner[0] + corner[1]:
                turn_n = 'up'
                choose_n = corner[1]

                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            elif corner[0] + corner[1] <= s_r < corner[0] + corner[1] + corner[2]:
                turn_n = 'down'
                choose_n = corner[2]

                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            elif corner[0] + corner[1] + corner[2] <= s_r < corner[0] + corner[1] + corner[2] + corner[3]:
                turn_n = 'right'
                choose_n = corner[3]

                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            # print('方向：', turn_n)
            turn_n_all.append(turn_n)
            choose_all.append(choose_n)

        ## 14
        #####方向顺序 front、behind、up、down、left、right
        elif ion_cor_10[i][0] == (2*N-1) and ion_cor_10[i][1] == 1 and 1 < ion_cor_10[i][2] < (2*N-1):
            # print('14:前左线，')
            # print('原坐标：',ion_cor_10[i])
            # arris_6.append(tao_all[i][1])  # behind、up、down、right
            # arris_6.append(tao_all[i][2])
            # arris_6.append(tao_all[i][3])
            # arris_6.append(tao_all[i][5])
            corner = [tao_all[i][1], tao_all[i][2], tao_all[i][3], tao_all[i][5]]
            # print('所有概率：', tao_all[i])
            # print('可选概率：1 2 3 5 ', arris_6)

            sum1 = sum(corner)
            # ran14 = random.uniform(0, 1)
            s_r = sum1 * ran

            if 0 <= s_r < corner[0]:
                turn_n = 'behind'
                choose_n = corner[0]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            elif corner[0] <= s_r < corner[0] + corner[1]:
                turn_n = 'up'
                choose_n = corner[1]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            elif corner[0] + corner[1] <= s_r < corner[0] + corner[1] + corner[2]:
                turn_n = 'down'
                choose_n = corner[2]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            elif corner[0] + corner[1] + corner[2] <= s_r < corner[0] + corner[1] + corner[2] + corner[3]:
                turn_n = 'right'
                choose_n = corner[3]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            # print('方向：', turn_n)
            turn_n_all.append(turn_n)
            choose_all.append(choose_n)

        ##15
        #####方向顺序 front、behind、up、down、left、right
        elif ion_cor_10[i][0] == ion_cor_10[i][1] == (2*N-1) and  1 < ion_cor_10[i][2] < (2*N-1):
            # print('15:前右线')
            # print('原坐标：',ion_cor_10[i])
            # arris_7.append(tao_all[i][1])  # behind、up、down、left
            # arris_7.append(tao_all[i][2])
            # arris_7.append(tao_all[i][3])
            # arris_7.append(tao_all[i][4])
            corner = [tao_all[i][1], tao_all[i][2], tao_all[i][3], tao_all[i][4]]
            # print('所有概率：', tao_all[i])
            # print('可选概率：1 2 3 4 ', arris_7)

            sum1 = sum(corner)
            # ran15 = random.uniform(0, 1)
            s_r = sum1 * ran

            if 0 <= s_r < corner[0]:
                turn_n = 'behind'
                choose_n = corner[0]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)

            elif corner[0] <= s_r < corner[0] + corner[1]:
                turn_n = 'up'
                choose_n = corner[1]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)

            elif corner[0] + corner[1] <= s_r < corner[0] + corner[1] + corner[2]:
                turn_n = 'down'
                choose_n = corner[2]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)

            elif corner[0] + corner[1] + corner[2] <= s_r < corner[0] + corner[1] + corner[2] + corner[3]:
                turn_n = 'left'
                choose_n = corner[3]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            # print('方向：', turn_n)
            turn_n_all.append(turn_n)
            choose_all.append(choose_n)

        ##16
        #####方向顺序 front、behind、up、down、left、right
        elif ion_cor_10[i][0] == 1 and ion_cor_10[i][1] == (2*N-1) and  1 < ion_cor_10[i][2] < (2*N-1):
            # print('16:右后线')
            # print('原坐标：',ion_cor_10[i])
            # arris_8.append(tao_all[i][0])  # front、up、down、left
            # arris_8.append(tao_all[i][2])
            # arris_8.append(tao_all[i][3])
            # arris_8.append(tao_all[i][4])
            corner = [tao_all[i][0], tao_all[i][2], tao_all[i][3], tao_all[i][4]]
            # print('所有概率：', tao_all[i])
            # print('可选概率：0 2 3 4 ', arris_8)

            sum1 = sum(corner)
            # ran16 = random.uniform(0, 1)
            s_r = sum1 * ran

            if 0 <= s_r < corner[0]:
                turn_n = 'front'
                choose_n = corner[0]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            elif corner[0] <= s_r < corner[0] + corner[1]:
                turn_n = 'up'
                choose_n = corner[1]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            elif corner[0] + corner[1] <= s_r < corner[0] + corner[1] + corner[2]:
                turn_n = 'down'
                choose_n = corner[2]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            elif corner[0] + corner[1] + corner[2] <= s_r < corner[0] + corner[1] + corner[2] + corner[3]:
                turn_n = 'left'
                choose_n = corner[3]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            # print('方向：', turn_n)
            turn_n_all.append(turn_n)
            choose_all.append(choose_n)

        ## 17
        #####方向顺序 front、behind、up、down、left 、right
        elif  1 <ion_cor_10[i][0] <(2*N-1) and ion_cor_10[i][1] == 1 and ion_cor_10[i][2] == (2*N-1):
            # print('17:右上线')
            # print('原坐标：',ion_cor_10[i])
            # arris_9.append(tao_all[i][0])  # front、behind、down、right
            # arris_9.append(tao_all[i][1])
            # arris_9.append(tao_all[i][3])
            # arris_9.append(tao_all[i][5])
            corner = [tao_all[i][0], tao_all[i][1], tao_all[i][3], tao_all[i][5]]
            # print('所有概率：', tao_all[i])
            # print('可选概率：0 1 3 5 ', arris_9)

            sum1 = sum(corner)
            # ran17 = random.uniform(0, 1)
            s_r = sum1 * ran

            if 0 <= s_r < corner[0]:
                turn_n = 'front'
                choose_n = corner[0]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            elif corner[0] <= s_r < corner[0] + corner[1]:
                turn_n = 'behind'
                choose_n = corner[1]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            elif corner[0] + corner[1] <= s_r < corner[0] + corner[1] + corner[2]:
                turn_n = 'down'
                choose_n = corner[2]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            elif corner[0] + corner[1] + corner[2] <= s_r < corner[0] + corner[1] + corner[2] + corner[3]:
                turn_n = 'right'
                choose_n = corner[3]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            # print('方向：', turn_n)
            turn_n_all.append(turn_n)
            choose_all.append(choose_n)

        ## 18
        #####方向顺序 front、behind、up、down、left、right
        elif ion_cor_10[i][0] == ion_cor_10[i][2] == (2*N-1) and  1 < ion_cor_10[i][1] < (2*N-1):
            # print('18:前上线,后下左右')
            # print('原坐标：',ion_cor_10[i])
            # arris_10.append(tao_all[i][1])  # behind、down、left、right
            # arris_10.append(tao_all[i][3])
            # arris_10.append(tao_all[i][4])
            # arris_10.append(tao_all[i][5])
            corner = [tao_all[i][1], tao_all[i][3], tao_all[i][4], tao_all[i][5]]
            # print('所有概率：', tao_all[i])
            # print('可选概率：1 3 4 5 ', arris_10)

            sum1 = sum(corner)
            # ran18 = random.uniform(0, 1)
            s_r = sum1 * ran

            if 0 <= s_r < corner[0]:
                turn_n = 'behind'
                choose_n = corner[0]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            elif corner[0] <= s_r < corner[0] + corner[1]:
                turn_n = 'down'
                choose_n = corner[1]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            elif corner[0] + corner[1] <= s_r < corner[0] + corner[1] + corner[2]:
                turn_n = 'left'
                choose_n = corner[2]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            elif corner[0] + corner[1] + corner[2] <= s_r < corner[0] + corner[1] + corner[2] + corner[3]:
                turn_n = 'right'
                choose_n = corner[3]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            # print('方向：', turn_n)
            turn_n_all.append(turn_n)
            choose_all.append(choose_n)

        ##19
        #####方向顺序 front、behind、up、down、left、right
        elif ion_cor_10[i][1] == ion_cor_10[i][2] == (2*N-1) and 1 < ion_cor_10[i][0] < (2*N-1):
            # print('19:右上线，前后下左')
            # print('原坐标：',ion_cor_10[i])
            # arris_11.append(tao_all[i][0])  # front、behind、down、left
            # arris_11.append(tao_all[i][1])
            # arris_11.append(tao_all[i][3])
            # arris_11.append(tao_all[i][4])
            corner = [tao_all[i][0], tao_all[i][1], tao_all[i][3], tao_all[i][4]]
            # print('所有概率：', tao_all[i])
            # print('可选概率：0 1 3 4 ', arris_11)

            sum1 = sum(corner)
            # ran19 = random.uniform(0, 1)
            s_r = sum1 * ran

            if 0 <= s_r < corner[0]:
                turn_n = 'front'
                choose_n = corner[0]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            elif corner[0] <= s_r < corner[0] + corner[1]:
                turn_n = 'behind'
                choose_n = corner[1]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            elif corner[0] + corner[1] <= s_r < corner[0] + corner[1] + corner[2]:
                turn_n = 'down'
                choose_n = corner[2]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            elif corner[0] + corner[1] + corner[2] <= s_r < corner[0] + corner[1] + corner[2] + corner[3]:
                turn_n = 'left'
                choose_n = corner[3]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            # print('方向：', turn_n)
            turn_n_all.append(turn_n)
            choose_all.append(choose_n)

        ## 20
        #####方向顺序 front、behind、up、down、left、right
        elif ion_cor_10[i][0] == 1 and ion_cor_10[i][2] == (2*N-1) and 1 < ion_cor_10[i][1] < (2*N-1):
            # print('20:后上线，前下左右')
            # print('原坐标：',ion_cor_10[i])
            # arris_12.append(tao_all[i][0])  # front、down、left、right
            # arris_12.append(tao_all[i][3])
            # arris_12.append(tao_all[i][4])
            # arris_12.append(tao_all[i][5])
            corner = [tao_all[i][0], tao_all[i][3], tao_all[i][4], tao_all[i][5]]
            # print('所有概率：', tao_all[i])
            # print('可选概率：0 3 4 5 ', arris_12)

            sum1 = sum(corner)
            ran = random.uniform(0, 1)
            s_r = sum1 * ran

            if 0 <= s_r < corner[0]:
                turn_n = 'front'
                choose_n = corner[0]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            elif corner[0] <= s_r < corner[0] + corner[1]:
                turn_n = 'down'
                choose_n = corner[1]
                # turn_n_all.append(turn_n)
                #                 # choose_all.append(choose_n)
            elif corner[0] + corner[1] <= s_r < corner[0] + corner[1] + corner[2]:
                turn_n = 'left'
                choose_n = corner[2]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            elif corner[0] + corner[1] + corner[2] <= s_r < corner[0] + corner[1] + corner[2] + corner[3]:
                turn_n = 'right'
                choose_n = corner[3]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            # print('方向：', turn_n)
            turn_n_all.append(turn_n)
            choose_all.append(choose_n)

        ## 21
        #####方向顺序 front、behind、up、down、left、right
        elif ion_cor_10[i][2] == 1 and 1 < ion_cor_10[i][0] < (2*N-1) and 1 < ion_cor_10[i][1] < (2*N-1):
            # print('21:下面，前后上左右')
            # print('原坐标：',ion_cor_10[i])
            # surface_1.append(tao_all[i][0])# front、behind、up、##down、left、right
            # surface_1.append(tao_all[i][1])
            # surface_1.append(tao_all[i][2])
            # surface_1.append(tao_all[i][4])
            # surface_1.append(tao_all[i][5])
            corner = [tao_all[i][0], tao_all[i][1], tao_all[i][2], tao_all[i][4],tao_all[i][5]]
            # print('所有概率：', tao_all[i])
            # print('可选概率：0 1 2 4 5 ', surface_1)

            sum1 = sum(corner)
            # ran21 = random.uniform(0, 1)
            s_r = sum1 * ran

            if 0 <= s_r < corner[0]:
                turn_n = 'front'
                choose_n = corner[0]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            elif corner[0] <= s_r < corner[0] + corner[1]:
                turn_n = 'behind'
                choose_n = corner[1]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            elif corner[0] + corner[1] <= s_r < corner[0] + corner[1] + corner[2]:
                turn_n = 'up'
                choose_n = corner[2]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            elif corner[0] + corner[1] + corner[2] <= s_r < corner[0] + corner[1] + corner[2] + corner[3]:
                turn_n = 'left'
                choose_n = corner[3]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            elif corner[0] + corner[1] + corner[2] + corner[3] <= s_r < corner[0] + corner[1] + corner[2] + corner[3] + corner[4]:
                turn_n = 'right'
                choose_n = corner[4]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            # print('方向：', turn_n)
            turn_n_all.append(turn_n)
            choose_all.append(choose_n)

        ## 22
        #####方向顺序 front、behind、up、down、left、right
        elif ion_cor_10[i][2] == (2*N-1) and 1 < ion_cor_10[i][0] < (2*N-1) and 1 < ion_cor_10[i][1] < (2*N-1):
            # print('22:上面,前后下左右')
            # print('原坐标：',ion_cor_10[i])
            # surface_2.append(tao_all[i][0]) # front、behind、##up、down、left、right
            # surface_2.append(tao_all[i][1])
            # surface_2.append(tao_all[i][3])
            # surface_2.append(tao_all[i][4])
            # surface_2.append(tao_all[i][5])
            corner = [tao_all[i][0], tao_all[i][1], tao_all[i][3], tao_all[i][4], tao_all[i][5]]
            # print('所有概率：', tao_all[i])
            # print('可选概率：0 1 3 4 5 ', surface_2)

            sum1 = sum(corner)
            # ran = random.uniform(0, 1)
            s_r = sum1 * ran

            if 0 <= s_r < corner[0]:
                turn_n = 'front'
                choose_n = corner[0]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            elif corner[0] <= s_r < corner[0] + corner[1]:
                turn_n = 'behind'
                choose_n = corner[1]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            elif corner[0] + corner[1] <= s_r < corner[0] + corner[1] + corner[2]:
                turn_n = 'down'
                choose_n = corner[2]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            elif corner[0] + corner[1] + corner[2] <= s_r < corner[0] + corner[1] + corner[2] + corner[3]:
                turn_n = 'left'
                choose_n = corner[3]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            elif corner[0] + corner[1] + corner[2] + corner[3] <= s_r < corner[0] + corner[1] + corner[2] + corner[3] + corner[4]:
                turn_n = 'right'
                choose_n = corner[4]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            # print('方向：', turn_n)
            turn_n_all.append(turn_n)
            choose_all.append(choose_n)

        ## 23
        #####方向顺序 front、behind、up、down、left、right
        elif ion_cor_10[i][0] == 1 and 1 < ion_cor_10[i][1] < (2*N-1) and 1 < ion_cor_10[i][2] < (2*N-1):
            # print('23:后面,前上下左右')
            # print('原坐标：',ion_cor_10[i])
            # surface_3.append(tao_all[i][0])# front、##behind、up、down、left、right
            # surface_3.append(tao_all[i][2])
            # surface_3.append(tao_all[i][3])
            # surface_3.append(tao_all[i][4])
            # surface_3.append(tao_all[i][5])
            corner = [tao_all[i][0], tao_all[i][2], tao_all[i][3], tao_all[i][4], tao_all[i][5]]
            # print('所有概率：', tao_all[i])
            # print('可选概率：0 2 3 4 5 ', surface_3)

            sum1 = sum(corner)
            # ran23 = random.uniform(0, 1)
            s_r = sum1 * ran

            if 0 <= s_r < corner[0]:
                turn_n = 'front'
                choose_n = corner[0]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            elif corner[0] <= s_r < corner[0] + corner[1]:
                turn_n = 'up'
                choose_n = corner[1]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            elif corner[0] + corner[1] <= s_r < corner[0] + corner[1] + corner[2]:
                turn_n = 'down'
                choose_n = corner[2]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            elif corner[0] + corner[1] + corner[2] <= s_r < corner[0] + corner[1] + corner[2] + corner[3]:
                turn_n = 'left'
                choose_n = corner[3]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            elif corner[0] + corner[1] + corner[2] + corner[3] <= s_r < corner[0] + corner[1] + corner[2] + corner[3] + corner[4]:
                turn_n = 'right'
                choose_n = corner[4]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            # print('方向：',turn_n)
            turn_n_all.append(turn_n)
            choose_all.append(choose_n)

        ## 24
        #####方向顺序 front、behind、up、down、left、right
        elif ion_cor_10[i][0] == (2*N-1) and 1 < ion_cor_10[i][1] < (2*N-1) and 1 < ion_cor_10[i][2] < (2*N-1):
            # print('24:前面,后上下左右')
            # print('原坐标：',ion_cor_10[i])
            # surface_4.append(tao_all[i][1])#  ##front、behind、up、down、left、right
            # surface_4.append(tao_all[i][2])
            # surface_4.append(tao_all[i][3])
            # surface_4.append(tao_all[i][4])
            # surface_4.append(tao_all[i][5])
            corner = [tao_all[i][1], tao_all[i][2], tao_all[i][3], tao_all[i][4], tao_all[i][5]]
            # print('所有概率：', tao_all[i])
            # print('可选概率：1 2 3 4 5 ', surface_4)

            sum1 = sum(corner)
            # ran24 = random.uniform(0, 1)
            s_r = sum1 * ran

            if 0 <= s_r < corner[0]:
                turn_n = 'behind'
                choose_n = corner[0]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            elif corner[0] <= s_r < corner[0] + corner[1]:
                turn_n = 'up'
                choose_n = corner[1]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            elif corner[0] + corner[1] <= s_r < corner[0] + corner[1] + corner[2]:
                turn_n = 'down'
                choose_n = corner[2]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            elif corner[0] + corner[1] + corner[2] <= s_r < corner[0] + corner[1] + corner[2] + corner[3]:
                turn_n = 'left'
                choose_n = corner[3]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            elif corner[0] + corner[1] + corner[2] + corner[3] <= s_r < corner[0] + corner[1] + corner[2] + corner[3] + corner[4]:
                turn_n = 'right'
                choose_n = corner[4]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            # print('方向：', turn_n)
            turn_n_all.append(turn_n)
            choose_all.append(choose_n)

        ## 25
        #####方向顺序 front、behind、up、down、left、right
        elif ion_cor_10[i][1] == 1 and 1 < ion_cor_10[i][0] < (2*N-1) and 1 < ion_cor_10[i][2] < (2*N-1):
            # print('25:左面,前后上下右')
            # print('原坐标：',ion_cor_10[i])
            # surface_5.append(tao_all[i][0])# front、behind、up、down、##left、right
            # surface_5.append(tao_all[i][1])
            # surface_5.append(tao_all[i][2])
            # surface_5.append(tao_all[i][3])
            # surface_5.append(tao_all[i][5])
            corner = [tao_all[i][0], tao_all[i][1], tao_all[i][2], tao_all[i][3], tao_all[i][5]]
            # print('所有概率：', tao_all[i])
            # print('可选概率：0 1 2 3 5 ', surface_5)

            sum1 = sum(corner)
            # ran25 = random.uniform(0, 1)
            s_r = sum1 * ran

            if 0 <= s_r < corner[0]:
                turn_n = 'front'
                choose_n = corner[0]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            elif corner[0] <= s_r < corner[0] + corner[1]:
                turn_n = 'behind'
                choose_n = corner[1]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            elif corner[0] + corner[1] <= s_r < corner[0] + corner[1] + corner[2]:
                turn_n = 'up'
                choose_n = corner[2]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            elif corner[0] + corner[1] + corner[2] <= s_r < corner[0] + corner[1] + corner[2] + corner[3]:
                turn_n = 'down'
                choose_n = corner[3]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            elif corner[0] + corner[1] + corner[2] + corner[3] <= s_r < corner[0] + corner[1] + corner[2] + corner[3] + corner[4]:
                turn_n = 'right'
                choose_n = corner[4]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            # print('方向：', turn_n)
            turn_n_all.append(turn_n)
            choose_all.append(choose_n)

        ## 26
        #####方向顺序 front、behind、up、down、left、right
        elif ion_cor_10[i][1] == (2*N-1) and 1 < ion_cor_10[i][0] < (2*N-1) and 1 < ion_cor_10[i][2] < (2*N-1):
            # print('26:右面,前后上下左')
            # print('原坐标：',ion_cor_10[i])
            # surface_6.append(tao_all[i][0])# front、behind、up、down、left、##right
            # surface_6.append(tao_all[i][1])
            # surface_6.append(tao_all[i][2])
            # surface_6.append(tao_all[i][3])
            # surface_6.append(tao_all[i][4])
            corner = [tao_all[i][0],tao_all[i][1], tao_all[i][2], tao_all[i][3], tao_all[i][4]]
            # print('所有概率：', tao_all[i])
            # print('可选概率：0 1 2 3 4 ', surface_6)

            sum1 = sum(corner)
            # ran26 = random.uniform(0, 1)
            s_r = sum1 * ran

            if 0 <= s_r < corner[0]:
                turn_n = 'front'
                choose_n = corner[0]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            elif corner[0] <= s_r < corner[0] + corner[1]:
                turn_n = 'behind'
                choose_n = corner[1]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            elif corner[0] + corner[1] <= s_r < corner[0] + corner[1] + corner[2]:
                turn_n = 'up'
                choose_n = corner[2]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            elif corner[0] + corner[1] + corner[2] <= s_r < corner[0] + corner[1] + corner[2] + corner[3]:
                turn_n = 'down'
                choose_n = corner[3]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            elif corner[0] + corner[1] + corner[2] + corner[3] <= s_r < corner[0] + corner[1] + corner[2] + corner[3] + corner[4]:
                turn_n = 'left'
                choose_n = corner[4]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            # print('方向：', turn_n)
            turn_n_all.append(turn_n)
            choose_all.append(choose_n)

        ## 27
        elif 1 < ion_cor_10[i][0] < (2*N-1) and 1 < ion_cor_10[i][1] < (2*N-1) and 1 < ion_cor_10[i][2] < (2*N-1):
            # print('27:体内')
            # print('原坐标：',ion_cor_10[i])
            tao_i_sum = sum(tao_all[i])
            # ran_num = random.uniform(0, 1)
            W_R = tao_i_sum * ran


            if 0 <= W_R < tao_all[i][0]:
                turn_n = 'front'
                choose_n = tao_all[i][0]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            elif tao_all[i][0] <= W_R < tao_all[i][0] + tao_all[i][1]:
                turn_n = 'behind'
                choose_n = tao_all[i][1]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)

            elif tao_all[i][0] + tao_all[i][1] <= W_R < tao_all[i][0] + tao_all[i][1] + tao_all[i][2]:
                turn_n = 'up'
                choose_n = tao_all[i][2]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)

            elif tao_all[i][0] + tao_all[i][1] + tao_all[i][2] <= W_R < tao_all[i][0] + tao_all[i][1] + tao_all[i][2] + tao_all[i][3]:
                turn_n = 'down'
                choose_n = tao_all[i][3]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)

            elif tao_all[i][0] + tao_all[i][1] + tao_all[i][2] + tao_all[i][3] <= W_R < tao_all[i][0] + tao_all[i][1] + tao_all[i][2] + tao_all[i][3] + tao_all[i][4]:
                turn_n = 'left'
                choose_n = tao_all[i][4]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)

            elif tao_all[i][0] + tao_all[i][1] + tao_all[i][2] + tao_all[i][3] + tao_all[i][4] <= W_R < tao_all[i][0] + tao_all[i][1] + tao_all[i][2] + tao_all[i][3] + tao_all[i][4] + tao_all[i][5]:
                turn_n = 'right'
                choose_n = tao_all[i][5]
                # turn_n_all.append(turn_n)
                # choose_all.append(choose_n)
            # print('方向：', turn_n)
            turn_n_all.append(turn_n)  ### 存放10个离子的跳跃方向
            choose_all.append(choose_n)  ### 存放10 个离子所选方向的跳跃概率

    # print('离子的初始坐标：',ion_cor_10)
    # print('所有离子的跳跃方向：',turn_n_all)
    new_cor_all = []
    for i in range(len(turn_n_all)):
        if turn_n_all[i] == 'front':  ###cor_front = []cor_behind = []cor_up = [] cor_down = [] cor_left = [] cor_right = []
            cor_update_n = np.array([ion_cor_10[i][0] + 2, ion_cor_10[i][1], ion_cor_10[i][2]])
        elif turn_n_all[i] == 'behind':
            cor_update_n = np.array([ion_cor_10[i][0] - 2, ion_cor_10[i][1], ion_cor_10[i][2]])
        elif turn_n_all[i] == 'up':
            cor_update_n = np.array([ion_cor_10[i][0], ion_cor_10[i][1], ion_cor_10[i][2] + 2])
        elif turn_n_all[i] == 'down':
            cor_update_n = np.array([ion_cor_10[i][0], ion_cor_10[i][1], ion_cor_10[i][2] - 2])
        elif turn_n_all[i] == 'left':
            cor_update_n = np.array([ion_cor_10[i][0], ion_cor_10[i][1] - 2, ion_cor_10[i][2]])
        elif turn_n_all[i] == 'right':
            cor_update_n = np.array([ion_cor_10[i][0], ion_cor_10[i][1] + 2, ion_cor_10[i][2]])


        new_cor_all.append(cor_update_n)
    np_tao = np.array(choose_all)  ###离子所选方向的跳跃概率
    np_allcor = np.array(new_cor_all)  ## 新坐标

    return ion_cor_10,np_tao,np_allcor  ## 初始坐标，tao,更新的坐标


if __name__ == '__main__':

    time1 = datetime.datetime.now()
    Ion_infor_all = []
    Ion_infor = []
    N = 5
    n0 = 0
    X = Y = Z = N
    P = 0.2
    Ion_num = 10
    tao_a = 2
    tao_b = 20000
    tao_c = 5000
    rate_hopping_a = 1/tao_a
    rate_hopping_b = 1/tao_b
    rate_hopping_c = 1/tao_c

    all_cor = []
    # for i in range(0,31):
    #     a = initial_stru(P, X, Y, Z)
    #     b = Ion_state(X, Y, Z, Ion_num)
    #     c = Ion_sitneig(b)
    #     d = Ion_surrounding(a, c)
    #     #####site_cor用来存放掺杂物所占据的位点坐标,cor2_total存放的是Ion_sitneig的返回值，即10组列表，每组包含离子周围的位点坐标
    #     ##
    #     e = Ion_surrounding_tao(d, rate_hopping_a, rate_hopping_b,rate_hopping_c)  ###w_zhanju  是Ion_surrounding的返回值  10组包含对离子周围掺杂物占据的判断
    #     f = Ion_choose(e,b,N)###存放的是离子6个方向的tao,共10组/ion_cor_10是10个离子坐标
        # print('无机纳米掺杂颗粒占据的位点坐标：', a)
        # print('离子的初始坐标：', b)
        # print('所有离子周围8个位点坐标：', c)
        # print('每个离子周围掺杂物占据的情况：', d)
        # print('每个离子6个方向的跳跃概率：',e)
        # print('每个离子选择的跳跃方向及该方向对应的概率：',f)
        # print(len(f[1]))
    a = initial_stru(P, X, Y, Z)
    b = Ion_state(X, Y, Z, Ion_num)
    c = Ion_sitneig(b)
    d = Ion_surrounding(a, c)
    #####site_cor用来存放掺杂物所占据的位点坐标,cor2_total存放的是Ion_sitneig的返回值，即10组列表，每组包含离子周围的位点坐标
    ##
    e = Ion_surrounding_tao(d, rate_hopping_a, rate_hopping_b,
                            rate_hopping_c)  ###w_zhanju  是Ion_surrounding的返回值  10组包含对离子周围掺杂物占据的判断
    f = Ion_choose(e, b, N)  ###存放的是离子6个方向的tao,共10组/ion_cor_10是10个离子坐标


    print('离子更新后的信息：', f)

    time2 = datetime.datetime.now()
    print(time2 - time1)

