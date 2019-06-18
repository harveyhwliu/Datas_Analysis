#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties

def test_matplotlib1():
    """
    11岁到  30岁   每年交男女朋友的折线图
    :return:
    """
    x = range(11,31,1)
    y = [1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]

    #设置图片的大小
    fig = plt.figure(figsize=(5,5))

    #指定x轴间隔
    plt.xticks(range(11,31,2))

    #设置显示的间隔，显示字符串，x坐标轴上数据显示旋转45°,设置中文显示

    my_font= FontProperties(fname="/System/Library/Fonts/PingFang.ttc",size=12)

    _x = ["{}岁".format(i) for i in x]
    plt.xticks(x[::3],_x[::3],rotation=45,fontproperties=my_font)

    #添加描述信息
    plt.xlabel(u"年龄",fontproperties=my_font)
    plt.ylabel(u"交朋友数据",fontproperties=my_font)
    plt.title(u"11岁到30岁的每年交男女朋友数统计图",fontproperties=my_font)

    #指定y轴间距
    # plt.yticks(range(min(y),max(y)))


    #设置网格,并设置网格透明度
    plt.grid(alpha=0.1)



    plt.plot(x,y)     # 传入x和y, 通过 plot绘制出折线图
    plt.show()


    #图片的保存
    fig.savefig("test01.png")

def main():
    test_matplotlib1()



if __name__ == "__main__":
    main()
