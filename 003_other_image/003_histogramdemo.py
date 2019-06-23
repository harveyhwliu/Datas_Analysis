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
    画 直方图
    :return:
    """
    x = [random.randrange(60,120) for x in range(100)]
    my_font= FontProperties(fname="/System/Library/Fonts/PingFang.ttc",size=12)
    fig = plt.figure(figsize=(10,8),dpi=50)#画板设置
    #1、 最简单的直方图
    # plt.hist(x,50)   #绘制直方图，传入统计数据 以及数组数即可
    #2、数据分成多少组
    d = 3  #组距
    num_bins = (max(x) - min(x))//d   # 组数,如果这里的num_bins 不是整除关系，就有问题，会有一些图像偏移
    print max(x),min(x),max(x)-min(x),d,num_bins
    #组距均匀，如果可以被整除，这设置为该组数，组距不均匀，即不能的化，需要进行调整间隔数或者采用其他方法
    plt.xticks(range(min(x),max(x)+d,d)) #设置间隔
    # plt.hist(x,num_bins)
    #频率分布直方图
    plt.hist(x,num_bins,normed=1)
    plt.xlabel(u"数据分组",fontproperties=my_font)   #x轴描述
    plt.ylabel(u"数据分布",fontproperties=my_font)#y轴描述
    plt.title(u"数据统计直方图",fontproperties=my_font)#图片标题
    plt.grid(alpha=0.4)      #设置网格,并设置网格透明度
    plt.show()               #图片展示
    fig.savefig("test03.png")#图片的保存


def test_matplotlib2():
    """
    画 直方图， 通过条形图修改width 来绘制  直方图
    :return:
    """
    interval = [0,5,10,15,20,25,30,35,40,45,60,90]   #时间间隔
    width = [5,5,5,5,5,5,5,5,5,15,30,60]             #分组间隔
    quantity = [836,2737,3723,3926,3596,1438,3273,643,824,613,215,47]
    my_font= FontProperties(fname="/System/Library/Fonts/PingFang.ttc",size=12)
    fig = plt.figure(figsize=(10,8),dpi=50)#画板设置

    plt.bar(range(len(interval)),quantity,width=1)

    _x = [i-0.5 for i in range(len(interval)+1)]
    x_tick_labels=interval+[150]
    plt.xticks(_x,x_tick_labels)

    plt.xlabel(u"数据分组",fontproperties=my_font)   #x轴描述
    plt.ylabel(u"数据分布",fontproperties=my_font)#y轴描述
    plt.title(u"数据统计直方图",fontproperties=my_font)#图片标题
    plt.grid(alpha=0.4)      #设置网格,并设置网格透明度
    plt.show()               #图片展示
    fig.savefig("test04.png")#图片的保存




def main():
    test_matplotlib2()



if __name__ == "__main__":
    main()
