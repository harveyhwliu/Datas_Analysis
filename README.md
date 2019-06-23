# Datas_Analysis


	1. 绘制散点图
		1. 绘图实例代码：
			i. y_3=[1+22*random.random()for_iinrange(31)]
			ii. y_10=[15+15*random.random()for_iinrange(31)]#10月气温
			iii. x=range(1,32)#3月份
			iv.
			v. x_interval=40#时间的间隔
			vi. x_10=[i+x_intervalforiinx]#10月份为了画图不重叠，需要空隔一段距离
			vii.
			viii. x_new=list(x)+list(x_10)#新的x轴坐标，为了设置X轴的间隔而设计
			ix.
			x. _xticks_labels=[u"3月{}日".format(i)foriinx]#设置xticks的显示效果
			xi. _xticks_labels+=[u"10月{}日".format(i-x_interval)foriinx_10]
			xii.
			xiii. my_font=FontProperties(fname="/System/Library/Fonts/PingFang.ttc",size=12)
			xiv. fig=plt.figure(figsize=(10,8),dpi=50)#画板设置
			xv. plt.xticks(x_new[::3],_xticks_labels[::3],rotation=45,fontproperties=my_font)#设置x坐标间隔
			xvi.
			xvii. plt.scatter(x,y_3)#绘制散点图scatter
			xviii. plt.scatter(x_10,y_10)
			xix.
			xx. plt.xlabel(u"时间",fontproperties=my_font)#x轴描述
			xxi. plt.ylabel(u"气温分布",fontproperties=my_font)#y轴描述
			xxii. plt.title(u"3月份和10月份的气温散点图",fontproperties=my_font)#图片标题
			xxiii.
			xxiv. plt.grid(alpha=0.1)#设置网格,并设置网格透明度
			xxv. plt.show()#图片展示
			xxvi. fig.savefig("test01.png")#图片的保存
		2. 散点图  和  折线图的区别：
			i. 调用画图函数的API 不同，折线图是plot(),散点图是 scatter()




	2. 绘制条形图
		1.   竖型  和  横行
			i. customers=['小王','小李','小王八','小海龟太长\n厂厂厂厂厂商','小狗子']#x轴数据,如果标题太长，需要添加\n，显示效果更佳
			ii. customers_index=range(len(customers))#画条形图，需要传入对应的索引（转换为数字）
			iii. sale_amounts=[127,90,201,111,232]#y轴数据
			iv. _xticks_labels=[u"{}".format(i)foriincustomers]#设置xticks的显示效果，针对竖着的条形图
			v. _yticks_labels=[u"{}".format(i)foriincustomers]#设置yticks的显示效果,针对横着的条形图
			vi. my_font=FontProperties(fname="/System/Library/Fonts/PingFang.ttc",size=12)
			vii. fig=plt.figure(figsize=(10,8),dpi=50)#画板设置
			viii. #plt.xticks(customers_index,_xticks_labels,rotation=45,fontproperties=my_font)#设置x坐标间隔,针对竖着的条形图而设置的
			ix. #plt.bar(customers_index,sale_amounts,width=0.3)#绘制条形图bar,指定宽度，正常形态
			x. #plt.xlabel(u"客户",fontproperties=my_font)#x轴描述
			xi. #plt.ylabel(u"销售额",fontproperties=my_font)#y轴描述
			xii. #plt.title(u"客户对应的销售额分布",fontproperties=my_font)#图片标题
			xiii. plt.yticks(customers_index,_yticks_labels,fontproperties=my_font)#设置y坐标间隔
			xiv. plt.barh(customers_index,sale_amounts,height=0.3,color="orange")#绘制条形图bar,指定长度，横着的图像
			xv. plt.xlabel(u"销售额",fontproperties=my_font)#x轴描述
			xvi. plt.ylabel(u"客户",fontproperties=my_font)#y轴描述
			xvii. plt.title(u"客户对应的销售额分布",fontproperties=my_font)#图片标题
			xviii. plt.grid(alpha=0.4)#设置网格,并设置网格透明度
			xix. plt.show()#图片展示
			xx. fig.savefig("test02.png")#图片的保存
		2. 条形图的对比：
			i. customers=['猩球崛起3：终极之战','敦刻尔克','蜘蛛侠：英雄归来','战狼2']#x轴数据,如果标题太长，需要添加\n，显示效果更佳
			ii. bar_width=0.2
			iii. customers_index_16=range(len(customers))
			iv. customers_index_15=[i+bar_widthforiincustomers_index_16]#x轴进行右移
			v. customers_index_14=[i+bar_width*2foriincustomers_index_16]
			vi. sale_amounts_16=[15746,312,4497,319]#y轴数据
			vii. sale_amounts_15=[12357,156,2045,168]
			viii. sale_amounts_14=[2358,399,2358,362]
			ix.
			x. _xticks_labels=[u"{}".format(i)foriincustomers]#设置xticks的显示效果，针对竖着的条形图
			xi. my_font=FontProperties(fname="/System/Library/Fonts/PingFang.ttc",size=12)
			xii. fig=plt.figure(figsize=(10,8),dpi=50)#画板设置
			xiii. plt.xticks(customers_index_15,_xticks_labels,fontproperties=my_font)#设置x坐标间隔,针对竖着的条形图而设置的
			xiv. plt.bar(customers_index_16,sale_amounts_16,width=bar_width,color="red",label="16日")#绘制条形图bar,指定宽度，正常形态
			xv. plt.bar(customers_index_15,sale_amounts_15,width=bar_width,color="blue",label="15日")#绘制条形图bar,指定宽度，正常形态
			xvi. plt.bar(customers_index_14,sale_amounts_14,width=bar_width,color="orange",label="14日")#绘制条形图bar,指定宽度，正常形态
			xvii. plt.xlabel(u"电影名称",fontproperties=my_font)#x轴描述
			xviii. plt.ylabel(u"票房",fontproperties=my_font)#y轴描述
			xix. plt.title(u"14,15,16日电影与对应的票房分布",fontproperties=my_font)#图片标题
			xx. plt.legend(prop=my_font)
			xxi. plt.grid(alpha=0.4)#设置网格,并设置网格透明度
			xxii. plt.show()#图片展示
			xxiii. fig.savefig("test022.png")#图片的保存
			xxiv.
		3. 说明：
			i.  竖型条形图 bar ,  横行条形图 barh (  注意参数width,height 设置等)
			ii. 对比条形图，需要考虑让x轴移动一段距离，假设需要画x组对比图，每个图宽width ,则 width*x <1
			iii. 对比条形图，设置xticks 或者y ticks 的时候，仅需要设置处理 （x/2） 这个条形图的间隔就行了
			iv. 需要给多组条形图添加图例



	3.   直方图： 数据分组统计
		1. 组距  =  （极差） /(组距 )     ，极差 = max(x) - min（x）
		2. 使用hist 绘图
		3. 没有经过统计的原始数据才能进行绘制  直方图（hist方法）
			x=[random.randrange(60,120)forxinrange(100)]
			my_font=FontProperties(fname="/System/Library/Fonts/PingFang.ttc",size=12)
			fig=plt.figure(figsize=(10,8),dpi=50)#画板设置
			#1、最简单的直方图
			#plt.hist(x,50)#绘制直方图，传入统计数据以及数组数即可
			#2、数据分成多少组
			d=3#组距
			num_bins=(max(x)-min(x))//d#组数,如果这里的num_bins不是整除关系，就有问题，会有一些图像偏移
			printmax(x),min(x),max(x)-min(x),d,num_bins
			#组距均匀，如果可以被整除，这设置为该组数，组距不均匀，即不能的化，需要进行调整间隔数或者采用其他方法
			plt.xticks(range(min(x),max(x)+d,d))#设置间隔
			#plt.hist(x,num_bins)
			#频率分布直方图
			plt.hist(x,num_bins,normed=1)
			plt.xlabel(u"数据分组",fontproperties=my_font)#x轴描述
			plt.ylabel(u"数据分布",fontproperties=my_font)#y轴描述
			plt.title(u"数据统计直方图",fontproperties=my_font)#图片标题
			plt.grid(alpha=0.4)#设置网格,并设置网格透明度
			plt.show()#图片展示
			fig.savefig("test03.png")#图片的保存

		4. 频率分布直方图，是直方图基础上，通过normed=1来绘制的
			interval=[0,5,10,15,20,25,30,35,40,45,60,90]#时间间隔
			width=[5,5,5,5,5,5,5,5,5,15,30,60]#分组间隔
			quantity=[836,2737,3723,3926,3596,1438,3273,643,824,613,215,47]
			my_font=FontProperties(fname="/System/Library/Fonts/PingFang.ttc",size=12)
			fig=plt.figure(figsize=(10,8),dpi=50)#画板设置

			plt.bar(range(len(interval)),quantity,width=1)

			_x=[i-0.5foriinrange(len(interval)+1)]
			x_tick_labels=interval+[150]
			plt.xticks(_x,x_tick_labels)

			plt.xlabel(u"数据分组",fontproperties=my_font)#x轴描述
			plt.ylabel(u"数据分布",fontproperties=my_font)#y轴描述
			plt.title(u"数据统计直方图",fontproperties=my_font)#图片标题
			plt.grid(alpha=0.4)#设置网格,并设置网格透明度
			plt.show()#图片展示
			fig.savefig("test04.png")#图片的保存







	4. 扩展
		1. Echarts.baidu.com    前端工具
		2. plotly   可视化工具中的github,相比较matplotlib 更简单         plot.ly/python
		3.
		4.
