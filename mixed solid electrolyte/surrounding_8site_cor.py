from initiating_structure import Ion_state as Ion_state
from initiating_structure import initial_stru as initial_stru
import datetime
import numpy as np
#### 模块功能 #找出包围离子的8个小方块的坐标


###将函数形参改成坐标形式输入
def Ion_sitneig(cor_all_10):#找出包围离子的8个小方块的坐标

    ###存放的是10个离子坐标
    ###下面程序是找出包围离子的8个小方块的坐标

    # cor_total = []
    cor1_total = []
    for cor in cor_all_10:  ##找出包围离子的8个小方格的坐标
        x_1 = cor[0] - 1
        x_2 = cor[0] + 1
        y_1 = cor[1] - 1
        y_2 = cor[1] + 1
        z_1 = cor[2] - 1
        z_2 = cor[2] + 1
        # cor0.append(x_1)
        # cor0.append(y_1)  ###以(1，1，1)为例
        # cor0.append(z_1)  ###cor0(0,0,0)
        cor0 = np.array([x_1,y_1,z_1])        # print(cor0)  ##这条语句循环了4次，8组坐标为一次，每组坐标包含（cor1-cor8）
        # cor_total.append(cor0)
        # cor1.append(x_1)
        # cor1.append(y_1)
        # cor1.append(z_2)  ###cor1(0,0,2)
        cor1 = np.array([x_1,y_1,z_2])
        # print(cor1)
        # cor_total.append(cor1)
        # cor2.append(x_1)
        # cor2.append(y_2)
        # cor2.append(z_1)  ###cor2(0,2,0)
        cor2 = np.array([x_1,y_2,z_1])
        # print(cor2)
        # cor_total.append(cor2)
        # cor3.append(x_1)
        # cor3.append(y_2)
        # cor3.append(z_2)  ###cor3(0,2,2)
        cor3 = np.array([x_1,y_2,z_2])
        # print(cor3)
        # cor_total.append(cor3)
        # cor4.append(x_2)
        # cor4.append(y_1)
        # cor4.append(z_1)  ##cor4(2,0,0)
        cor4 = np.array([x_2,y_1,z_1])
        # print(cor4)
        # cor_total.append(cor4)
        # cor5.append(x_2)
        # cor5.append(y_1)
        # cor5.append(z_2)  ###cor5(2,0,2)
        cor5 = np.array([x_2,y_1,z_2])
        # print(cor5)
        # cor_total.append(cor5)
        # cor6.append(x_2)
        # cor6.append(y_2)
        # cor6.append(z_1)  ###cor6(2,2,0)
        cor6 = np.array([x_2,y_2,z_1])
        # print(cor6)
        # cor_total.append(cor6)
        # cor7.append(x_2)
        # cor7.append(y_2)
        # cor7.append(z_2)  ###cor7(2,2,2)
        cor7 = np.array([x_2,y_2,z_2])
        # print(cor7)
        cor_total = np.array([cor0,cor1,cor2 ,cor3,cor4 ,cor5 ,cor6 ,cor7])

        cor1_total.append(cor_total)
        # cor_total = []  ###分别找出离子所在给点周围的8个方格的坐标
        #print('包围离子的8个小方块的坐标：')
        #print(cor1_total)
    cor2_total = np.array(cor1_total)

    # print('所有离子周围的八个小方块坐标：')
    # print(cor2_total)
    return cor2_total  ### 10个离子的周围8个位点坐标

if __name__ == '__main__':
    time1 = datetime.datetime.now()
    Ion_infor_all = []
    Ion_infor = []
    N = 5
    n0 = 0
    X = Y = Z = 5
    P = 0.08
    Ion_num = 10
    a = initial_stru(P,X,Y,Z)
    b = Ion_state(X,Y,Z,Ion_num)
    c = Ion_sitneig(b)

    # print('LLZO占据的位点坐标：', a)
    print('离子的初始坐标：', b)
    print('所有离子周围8个位点坐标：',c)
    print('len():',len(c))
    time2 = datetime.datetime.now()
    print(time2 - time1)
