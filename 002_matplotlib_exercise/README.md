## ***小结2***

	1. 背景：
		a. 岗位需求
		b. 是Python 数据科学的基础
		c. 是机器学习的课程基础

	2. 什么是数据分析
		a. 数据分析是适当的方法对收集来的大量数据进行分析，帮助人们做出判断，以便采取适当行动
		b. 常用工具：
			i. matplotlib
			ii. numpy
			iii. pandas

	3. 数据分析的流程：
		a. 提出问题
		b. 准备数据
			i. 数据预处理等
		c. 分析数据
		d. 获得结论
		e. 成果可视化
			i. 图形
			ii. 图表
			iii.
	4. 环境安装 ：
		a. conda环境安装
			i. conda:  data science package     &  environment manager
			ii. 创建环境：
				1) conda create   --name python3 python=3
				2) 切换环境：
					a) windows:    acitvate python3
					b) linux/macos: source activate  python3
				3) 官方地址：
					a) https://www.anaconda.com/download

		b. jupyter   notebook
			i. 一款编程，文档，笔记，展示软件
			ii. 启动命令   jupyter notebook
			iii. 安装Ipython    :  pip install Ipython     （要求python版本为python 3）

	5. matplotlib 介绍：
		a. 主要应用目的：
			i. matplotlib 能将数据进行可视化，更直观的呈现
			ii. 使数据更加客观，更具说服力
			iii. 最流行的Python底层绘图库，主要做数据可视化图表，名字取材于Matlab,模仿Matlab构建
		b. 基本要点：
			i. demo:
				1)  from matplotlib import pyplot as plt
				2) x = range(2,26,2)     #x轴，是一个可迭代对象
				3) y = [15,13,14,5,17,20,25,26,24,22,18,15]    #y轴，是一个可迭代对象
				4) plt.plot(x,y)     # 传入x和y, 通过 plot绘制出折线图
				5) plt.show()

			ii. 其他要点 ：
				1) 设置图片大小
					a) fig = plt.figure(figsize=(20,8),dpi=80)
					b) 图像大小为长20，宽8，   像素为80dpi

				2) 保存到本地
					a) fig.savefig(".test.png")       保存为图片
					b) 可以保存为svg这种矢量图格式，放大不会有锯齿

				3) 描述信息，比如X轴和Y轴表示什么，图表示什么
					1) my_font=FontProperties(fname="/System/Library/Fonts/PingFang.ttc",size=12)
					2) plt.xlabel("时间",fontproperties=my_font)
					3) plt.ylabel("温度单位（℃）",fontproperties=my_font)
					4) plt.title("10点到12点每分钟的气温图",fontproperties=my_font)

				4) 调整x或者y的刻度的间距
					1) plt.xticks(range(2,26,2))   #指定x轴间隔
					2) plt.yticks(range(5,30))      #指定y轴间距
					3) plt.yticks(range(min(y),max(y)))


				5) 线条的样式（比如颜色，透明度等）
					1) 绘制网格     plt.grid()
					2) 绘制网格，并制定透明度效果   plt.grid(alpha=0.4)
					3) 设置图例：
						i) my_font=FontProperties(fname="/System/Library/Fonts/PingFang.ttc",size=12)
						ii) plt.plot(x,y,label="图例1")
						iii) plt.legend(prop=my_font,loc=1)    指定图例位置，指定中文字体，注意只有图例这里是使用prop
					4) 指定画图颜色，线宽等属性
						1) plt.plot(x,y,label="自己",color="r",linestyle="--",linewidth=5,alpha=0.5)
						2) 网格grid()也可以指定线相关的属性，比如linestyle


				6) 标记处特殊的点（比如告诉别人最高点和最低点在哪里）
					1)
					2) #获取最大值最小值的索引
					3) max_indx=y.index(max(y))
					4) #设置最大值
					5) plt.plot(x[max_indx],y[max_indx],'ks')
					6) #显示最大值
					7) show_max='['+str(x[max_indx])+','+str(y[max_indx])+']'
					8) plt.annotate(show_max,xytext=(x[max_indx],y[max_indx]),xy=(x[max_indx],y[max_indx]))
					9)
				7) 给图片添加一个水印（防伪，防盗用）
					1)  fig.text(0.6,0.5,u'测试水印功能',fontsize=40,color='gray',ha='right',va='top',alpha=0.8,fontproperties=my_font)

				8) matplotlib默认不支持中文字符，因为默认的英文字体无法显示汉字
					1) 查看  linux/mac下面支持的字体
					2) fc-list    #查看支持的字体
					3) fc-list:lang=zh   #查看支持的中文（冒号前面有空格）
					4) 修改matplotlib的默认字体：
						i) 通过matplotlib.rc可以修改(针对Windows/liunx)
							i) #设置中文显示linux/windows下设置字体的方式
							ii) font={'family':'MicroSoftYaHei',
							iii) 'weight':'bold',
							iv) 'size':'larger'
							v) matplotlib.rc('font',**font)
							vi) #rc("font",family="MicroSoftYaHei","weight"="blod")

						ii) 通过matplotlib下的font_manager 可以解决(通用)
							One. from matplotlib import font_manager
		c. 总结：















