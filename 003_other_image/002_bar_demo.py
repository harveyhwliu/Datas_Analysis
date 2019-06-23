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
    画 条形图  竖着的条形图 bar 和  横着的条形图  barh
    :return:
    """
    customers = ['小王','小李','小王八','小海龟太长\n厂厂厂厂厂商','小狗子']   #x轴数据,如果标题太长，需要添加\n，显示效果更佳
    customers_index = range(len(customers))       #画条形图，需要传入对应的索引（转换为数字）
    sale_amounts = [127,90,201,111,232]           #y轴数据
    _xticks_labels = [u"{}".format(i) for i in customers]     #设置xticks 的 显示效果，针对竖着的条形图
    _yticks_labels = [u"{}".format(i) for i in customers]     #设置yticks 的 显示效果,针对横着的条形图
    my_font= FontProperties(fname="/System/Library/Fonts/PingFang.ttc",size=12)
    fig = plt.figure(figsize=(10,8),dpi=50)#画板设置
    # plt.xticks(customers_index,_xticks_labels,rotation=45,fontproperties=my_font)  #设置x坐标间隔,针对竖着的条形图而设置的
    # plt.bar(customers_index,sale_amounts,width=0.3)   #绘制条形图  bar,指定宽度 ， 正常形态
    # plt.xlabel(u"客户",fontproperties=my_font)   #x轴描述
    # plt.ylabel(u"销售额",fontproperties=my_font)#y轴描述
    # plt.title(u"客户对应的销售额分布",fontproperties=my_font)#图片标题
    plt.yticks(customers_index,_yticks_labels,fontproperties=my_font)  #设置y坐标间隔
    plt.barh(customers_index,sale_amounts,height=0.3,color="orange")   #绘制条形图  bar,指定长度 ， 横着的图像
    plt.xlabel(u"销售额",fontproperties=my_font)   #x轴描述
    plt.ylabel(u"客户",fontproperties=my_font)#y轴描述
    plt.title(u"客户对应的销售额分布",fontproperties=my_font)#图片标题
    plt.grid(alpha=0.4)      #设置网格,并设置网格透明度
    plt.show()               #图片展示
    fig.savefig("test02.png")#图片的保存


def test_matplotlib2():
    """
    画 条形图
    :return:
    """
    customers = ['猩球崛起3：终极之战','敦刻尔克','蜘蛛侠：英雄归来','战狼2']   #x轴数据,如果标题太长，需要添加\n，显示效果更佳
    bar_width = 0.2
    customers_index_16 = range(len(customers))
    customers_index_15 = [i+bar_width for i in customers_index_16]        #x轴进行右移
    customers_index_14 = [i+bar_width*2 for i in customers_index_16]
    sale_amounts_16 = [15746,312,4497,319]        #y轴数据
    sale_amounts_15 = [12357,156,2045,168]
    sale_amounts_14 = [2358,399,2358,362]

    _xticks_labels = [u"{}".format(i) for i in customers]     #设置xticks 的 显示效果，针对竖着的条形图
    my_font= FontProperties(fname="/System/Library/Fonts/PingFang.ttc",size=12)
    fig = plt.figure(figsize=(10,8),dpi=50)#画板设置
    plt.xticks(customers_index_15,_xticks_labels,fontproperties=my_font)  #设置x坐标间隔,针对竖着的条形图而设置的
    plt.bar(customers_index_16,sale_amounts_16,width=bar_width,color="red",label="16日")   #绘制条形图  bar,指定宽度 ， 正常形态
    plt.bar(customers_index_15,sale_amounts_15,width=bar_width,color="blue",label="15日")   #绘制条形图  bar,指定宽度 ， 正常形态
    plt.bar(customers_index_14,sale_amounts_14,width=bar_width,color="orange",label="14日")   #绘制条形图  bar,指定宽度 ， 正常形态
    plt.xlabel(u"电影名称",fontproperties=my_font)   #x轴描述
    plt.ylabel(u"票房",fontproperties=my_font)#y轴描述
    plt.title(u"14,15,16日电影与对应的票房分布",fontproperties=my_font)#图片标题
    plt.legend(prop = my_font)
    plt.grid(alpha=0.4)      #设置网格,并设置网格透明度
    plt.show()               #图片展示
    fig.savefig("test022.png")#图片的保存



def main():
    test_matplotlib2()



if __name__ == "__main__":
    main()
