#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties
import random

def test_matplotlib1():
    """
    画散点图   和 折线图的绘制的区别是 api从plot 变成了  scatter
    :return:
    """
    y_3  = [1+22*random.random()  for _i in range(31)]
    y_10  = [15+15*random.random() for _i in range(31)]# 10月气温

    x = range(1,32)  #3月份

    x_interval = 40                   #时间的间隔
    x_10 = [i+x_interval for i in x]  #10月份 为了画图不重叠，需要空隔一段距离

    x_new = list(x) + list(x_10)      #新的x轴坐标，为了设置X轴的间隔而设计

    _xticks_labels = [u"3月{}日".format(i) for i in x]     #设置xticks 的 显示效果
    _xticks_labels +=[u"10月{}日".format(i-x_interval) for i in x_10]

    my_font= FontProperties(fname="/System/Library/Fonts/PingFang.ttc",size=12)
    fig = plt.figure(figsize=(10,8),dpi=50)#画板设置
    plt.xticks(x_new[::3],_xticks_labels[::3],rotation=45,fontproperties=my_font)  #设置x坐标间隔

    plt.scatter(x,y_3)        #绘制散点图  scatter
    plt.scatter(x_10,y_10)

    plt.xlabel(u"时间",fontproperties=my_font)   #x轴描述
    plt.ylabel(u"气温分布",fontproperties=my_font)#y轴描述
    plt.title(u"3月份和10月份的气温散点图",fontproperties=my_font)#图片标题

    plt.grid(alpha=0.1)      #设置网格,并设置网格透明度
    plt.show()               #图片展示
    fig.savefig("test01.png")#图片的保存

def main():
    test_matplotlib1()



if __name__ == "__main__":
    main()
