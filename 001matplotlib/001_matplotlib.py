#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from matplotlib import pyplot as plt
import random
import json
import matplotlib
from matplotlib.font_manager import FontProperties




#设置中文显示    linux / windows下设置字体的方式
# font = {'family' : 'MicroSoft YaHei',
#           'weight': 'bold',
#           'size': 'larger'}
#
# matplotlib.rc('font', **font)

# matplotlib.rc("font",family="MicroSoft YaHei",weight="blod")



def test_matplotlib():
    x = range(2,26,2)     #x轴，是一个可迭代对象
    y = [15,13,14,5,17,20,25,26,24,22,18,15]    #y轴，是一个可迭代对象

    #设置图片的大小
    fig = plt.figure(figsize=(5,5))

    #指定x轴间隔
    plt.xticks(range(2,26,2))

    #指定y轴间距
    # plt.yticks(range(5,30))
    plt.yticks(range(min(y),max(y)))


    plt.plot(x,y)     # 传入x和y, 通过 plot绘制出折线图
    plt.show()


    #图片的保存
    fig.savefig(".test.png")



def test_matplotlib2():
    """
    如果列表啊表示10点到12点的每一分钟的气温，如何绘制折线图观察每分钟气温的变化情况？
    a=[random.randint(20,35) for i in range(120)]
    :return:
    """
    x = range(10*60,12*60,1)
    y = [random.randint(20,35) for i in range(120)]

    #设置图片的大小
    fig = plt.figure(figsize=(5,5))

    #指定x轴间隔
    # plt.xticks(range(10*60,12*60,5))
    #x轴显示字符串
    _x = [u"10点{}分".format(i) for i in range(60)]
    _x += [u"11点{}分".format(i) for i in range(60)]

    # print json.dumps(_x,ensure_ascii=False)
    #
    # print type(x[::1])
    # print type(_x[::1])

    #设置显示的间隔，显示字符串，x坐标轴上数据显示旋转45°,设置中文显示

    my_font= FontProperties(fname="/System/Library/Fonts/PingFang.ttc",size=12)


    plt.xticks(x[::3],_x[::3],rotation=45,fontproperties=my_font)

    #添加描述信息
    plt.xlabel(u"时间",fontproperties=my_font)

    plt.ylabel(u"温度单位（℃）",fontproperties=my_font)

    plt.title(u"10点到12点每分钟的气温图",fontproperties=my_font)
    #指定y轴间距
    # plt.yticks(range(min(y),max(y)))


    plt.plot(x,y)     # 传入x和y, 通过 plot绘制出折线图
    plt.show()


    #图片的保存
    fig.savefig(".test02.png")

def main():
    # test_matplotlib()
    test_matplotlib2()



if __name__ == "__main__":
    main()
