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
	print("Lebran's score is %d" %(d['Lebran']))
	
	#确认key值是否存在的方法1,通过in判断(输出为布尔类型)
	print('Thomas' in d)	#输出为False
	
	#确认key值是否存在的方法2,通过dict提供的get方法,如果key不存在,可以返回none,或者返回自己指定的value
	print(d.get('Thomas'))		#输出为None
	print(d.get('Thomas',-1))	#输出为-1
	
	#删除key可以使用pop(key)方法
	d.pop('Michael')
	print(d)

def set_test():
	#set和dict类似,也是一组key的集合,但不存储value,由于key不能重复,所以在set中,没有重复的key
	
	#创建一个set,需要提供一个list作为输入集合
	s = set([1,2,3,4,4,3,3,1,1,2])
	print(s)	#输出为 {1, 2, 3, 4},set会自动去掉重复的元素
	
	#向set添加元素,add(key)
	s.add(5)
	print(s)
	
	#从set中删除元素,remove(key)
	s.remove(1)
	print(s)
	
	#set由于没有重复元素,所以两个set可以求交集以及并集
	s1 = set([3,4,5,6,7,8])
	print(s1 & s)	#求两个set的交集
	print(s1 | s)	#求两个set的并集

#函数相关练习,定义空函数nop
def nop():
	pass

def my_abs(a):
	#检查传入的参数a是否是整型或浮点型
	if not isinstance(a,(int,float)):
		print('%r type false' %a)
		return -1
	if a >= 0:
		return a
	else:
		return -a
		
#返回多个值得函数
def move(x,y):
	if not isinstance(x,int):
		print('input value x(%r) type false' %x)
		retur -1,-1
	if not isinstance(y,int):
		print('input value y(%r) type false' %y)
	x = x + 2
	y = y + 2
	return x,y

#函数参数练习,计算x的n次方函数
def power(x,n):
	if not isinstance(x,int):
		print('input value x(%r) type false' %x)
	if not isinstance(n,int):
		print('input value n(%r) type false' %n)
	val = 1
	while(n > 0):
		val = val * x
		n = n - 1
	
	return val

#默认参数函数,调用函数可以传送第二个值,也可以不传送,如果不传送,第二个值默认为2
def power_deft(x,n=2):
	if not isinstance(x,int):
		print('input value x(%r) type false' %x)
	if not isinstance(n,int):
		print('input value n(%r) type false' %n)
	val = 1
	while(n > 0):
		val = val * x
		n = n - 1
	return val

#默认参数函数的坑
def add_end(l=[]):
	l.append('end')
	return l

#可变参数函数,可变参数函数为传入参数个数可变的函数,例如下面的函数用于求传入整数数组的和,
#在可变参数内部,函数接收到的是一个tuple值
def calc_list(numbers):
	#本函数不是可变参数函数,输入参数numbers为一个list
	sum = 0
	for i in numbers:
		sum = sum + i
	
	return sum

def calc_val(*numbers):
	#本函数为可变参数函数,只是在输入参数前加了个*
	sum = 0
	for i in numbers:
		sum = sum + i
	
	return sum

#关键字参数,关键字参数函数和可变参数函数的区别为关键字参数会将传入的值作为一个dict变量,声明时在参数前有两个*
def person(name,age,**kw):
	#在该函数中,name和age为必选参数,kw为可选参数
	print('name:',name,'age:',age,'other:',kw)

#命名关键字参数
#对于关键字参数,函数调用者可以传入任何不受限制的关键字参数,命名关键字参数可以限制关键字的名字
def person_name(name,age,*,city,job):
	#本函数中,name和age为必选参数,city和job为关键字名称,该函数也只能接受这两个额外的关键字参数
	print('name',name,'age',age,'city',city,'job',job)

#下面函数调用为正确格式
#person_name('Kobe',30,job = 'baskeyball player',city = 'Los')

#下面函数调用错误,必须传入job和city两个关键字的值
#person_name('Kobe',30)

#下面的函数调用错误,person_name函数只接受关键字job和city
#person_name('Tracy',30,job = 'baskeyball player',country = 'American')


#如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
def person(name, age, *args, city, job):
    print(name, age, args, city, job)

#命名关键字参数也可以使用默认参数,有了默认参数的关键字就可以不用传值了
def person_default(name,age,*,city = 'Beijing',job = 'IT'):
	print(name,age,city,job)

person_default('Kevin',29)

#io_test()
#list_test()
#tuple_test()
#if_test()
#loop_test()
#dict_test()
#set_test()
#print(my_abs(-12.34))
#x,y = move(1.1,2)
#print(x,y)
#print(power(2,10))
#print('power_deft(2) = %d' %(power_deft(2)))
#print('power_deft(2,4) = %d' %(power_deft(2,4)))

#print(add_end([1,2,3,4]))
#print(add_end([]))
#print(add_end([]))

#可变参数函数测试
#print(calc_list([1,2,5,67,9]))
#numbers = [1,2,3,4,5,6,7]
#print(calc_list(numbers))

#print(calc_val(1,4,56,6))
#print(calc_val(*numbers))

#关键字函数测试
#person('guoguo','30')		#输出为 name: guoguo age: 30 other: {}
#person('Jams','33',job = 'Calas',country = 'American') #输出为 name: Jams age: 33 other: {'country': 'American', 'job': 'Calas'}


