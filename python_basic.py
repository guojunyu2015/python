#!/usr/bin/python3.5

######################################################
##	文件名:		python_basic.py
##	文件说明:	python基础及函数练习,所有相关知识点均封装在函数中,调用函数来练习
##	创建时间:	2017年7月2日20:37:52
######################################################

#io_test函数用于主要用于练习常用的IO函数
def io_test():
	#input函数为从标准输入获取一个值,默认的类型为字符串,如果需要将其作为整数处理,需要使用int()函数将其转换为整数
	name = input("please input your name:")
	
	#print测试,%后跟类型修饰符,和C语言类似
	print("hello %s,your %dst python program" %(name,1))
	
	#格式化输出练习
	print("%05d" %1)	#输出数值1,左补零,结果为00001
	print("%.4s" %("12345")) #类似于C语言,输出时, .后面的为最大输出长度,.前面的为最小输出长度
	print("[%5s]" %("123"))    #最小输出长度为5,默认输出为左补空格
	print("[%-5s]" %("123"))	 #最小输出长度为5,%后加-,则成为右补空格
	
	pi = 3.1415926
	print("[%f]" %(pi))	#浮点数输出,默认为精确到小数点后6位
	print("[%10.2f]" %(pi))		#输出结果为 [      3.14],%10.2f意思为输出总长度为10,精确到小数点后2位,默认为左补空格
	print("[%-10.2f]" %(pi))	#输出结果为 [3.14      ]
	print("[%+.2f]" %(pi))		#显示输出值的正负号(主要用来显示正号,符号必须要直接显示出来)
		
	#布尔型数据测试,一个布尔值只有True和False两种值,以下输出为True False,布尔型值可以使用and or not三个运算符
	print(3>2,2>3,3>2 and 2<3)
	print("3>2's bool value is %r" %(3>2))


def list_test():
	#list为python内置的数据类型,list是一种有序的集合,可以随时添加删除其中的元素,定义list类型变量使用"[]"符号标识
	
	#定义list类型的变量classmates
	classmates = ['Michael','Bob','Tracy']
	print(classmates)	#可以使用print函数直接打印list变量
	print("%s" %(classmates))	#本打印语句效果同上面一句
	
	#获取list变量的元素个数
	print("the list val have %d element" %len(classmates))
	
	#可以用下标来访问list变量的元素,下标从0开始
	print("%s %s" %(classmates[0],classmates[1]))
	
	#下标-1指的是最后一个元素
	print("%s" %(classmates[-1]))
	
	#向list中追加元素到末尾
	classmates.append('Kobe')
	print(classmates)
	
	#把元素插入到指定位置
	classmates.insert(1,'Lebran')
	print(classmates)
	
	#删除list末尾的元素,使用pop()方法
	classmates.pop()
	print(classmates)
	
	#删除指定位置的元素,pop(i)
	classmates.pop(1)
	print(classmates)
	
	#把某个元素替换为其他元素,直接赋值即可
	classmates[1] = 'Lebran'
	print(classmates)
	
	#list中的元素的数据类型可以不同,list中的元素也可以是一个list变量

def tuple_test():
	#tuple和list类似,是一个有序的集合,声明时使用"()"符号,但是tuple一旦初始化就不能改变,它没有insert以及append这样的方法
	#访问tuple变量中的元素时直接用下标访问即可
	classmates = ('Lebran','Kyrie','Kevin')
	print("%s %s" %(classmates[0],classmates[1]))
	
	#如果只定义包含一个元素的tuple变量,由于tuple变量使用圆括号作为标识符,需要在变量后添加逗号
	#t = (1)	错误的定义方式,t会被解析成整型
	t = (1,)	#正确的定义方式,t为只包含一个元素的tuple变量	

def if_test():
	age = 20
	if(age >= 18):
		print("adult")
	elif(age >= 6):
		print("teenager")
	else:
		print("kid")
	

def loop_test():
	
	#for循环
	num = (1,2,3,4,5,6,7,8)
	sum = 0
	for i in num:
		sum = sum + i
	print("sum = %d" %sum)
	
	#如果要计算1到100的整数和
	print(range(10))
	print(list(range(10)))
	
	sum = 0
	for i in list(range(101)):
		sum = sum + i
	print("0-99 sum = %d" %sum)
	
	#while循环,类似于C,循环过程中可以使用break和continue,下面程序为计算100以内所有奇数的和
	n = 100
	sum = 0
	if(n % 2 == 0):
		n = n-1
	while(n > 0):
		sum = sum + n
		n = n-2
	print("100以内所有奇数的和为 %d" %sum)
	
def dict_test():
	#dict全称为dictionary,对应于java的map,使用键-值对存储数据,dict使用"{}"符号作为标识符
	
	#下面为用dict定义的存储姓名成绩的dict变量
	d = {'Michael':95,'Bob':75,'Tracy':85}
	print(d)	#输出整个dict变量的内容
	print(d['Michael'])		#输出Michael的成绩,注意符号
	
	#修改Bob的成绩为90
	d['Bob'] = 90
	print(d['Bob'])
	
	#Lebran关键字在dict中不存在,下面语句相当于将Lebran添加到dict中,成绩为98
	d['Lebran'] = 98
	print("Lebran's score is %d"d['Lebran'])
	
	#确认key值是否存在的方法1,通过in判断(输出为布尔类型)
	print('Thomas' in d)	#输出为False
	
	#确认key值是否存在的方法2,通过dict提供的get方法,如果key不存在,可以返回none,或者返回自己指定的value
	print(d.get('Thomas'))		#输出为None
	print(d.get('Thomas',-1))	#输出为-1
	
	#删除key可以使用pop(key)方法
	d.pop('Michael')
	print(d)
	
#下面为函数调用部分
#io_test()
#list_test()
#tuple_test()
#if_test()
#loop_test()
dict_test()
