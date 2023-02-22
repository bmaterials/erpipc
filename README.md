# pipc

#### 介绍

使用Python3编程语言开发了一个Python库pipc来实现复合聚合物固态电解质离子电导率的计算功能。

#### 软件架构
（1） initial_structure

   该模块实现了复合聚合物导体结构初始化的功能，包括模型尺寸大小，无机相的占据，walkers初始位点状态。

（2） ions_jumping_process
   
   该模块实现了walkers如何进行选择迁移的算法。

（3） samples_to_generate

   该模块用来记录walkers每一步迁移的信息，包括时间步长，位点坐标。

（4） parameter_calculation

   该模块实现离子电导率计算算法，通过所记录的足够多的walkers迁移信息，再根据能斯特爱因斯坦方程求解离子电导率。

#### 所需要的包

python 3.7.4 pandas 1.3.2 pip 21.2.2 python-dateutil 2.8.2 pytz 2021.1 setuptool 57.4.0 six 1.16.0

#### 使用方法
 
具体使用方法参考用户手册3.2节的参数设置运行。



