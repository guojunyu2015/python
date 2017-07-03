#!/usr/bin/python3.5

#input函数为从标准输入获取一个值,默认的类型为字符串,如果需要将其作为整数处理,需要使用int()函数将其转换为整数
#name=input('please input your name:')

#print测试,%后跟类型修饰符,和C语言类似
#print('hello,%s your %dst python program' %(name,1))

#print测试,如果要输出单引号,双引号等字符,用转义符即可
#print("hello,\'%s\'" %name)

#布尔型数据测试,一个布尔值只有True和False两种值,以下输出为True False
#print(3>2,4>5)

#布尔值可以用and or not运算,以下输出为True
#print(4 > 3 and 5 > 1)

#以下输出为False
#print(4 > 5 or 55 < 1)

#not是一个单目运算符,把True变成False,把False变成True,以下输出为True
#print(not 4 > 5)

#空值,空值是Python中的一个特殊的值,用None表示

#变量,python变量是什么类型要根据对其赋什么类型的值,以如下程序为例
#var_1 = 1
#print("var_1 = %d" %(var_1))

#var_1 = 'hehe'
#print("var_1 = %s" %(var_1))

#除法运算,/结果为浮点数,//为地板除,结果只保留整数部分,%为取余数,示例如下,输出结果为：3.3333333333333335 3 1
#print(10/3,10//3,10%3)

#字符编码,python中使用utf-8编码格式,在python中,可以使用ord函数获取字符的整数表示,chr函数把编码转换为对应的字符
#print("汉字\"国\"对应的utf-8编码为:%d" %(ord("国")))

#num = 69
#print("整数%d对应的字符为:%s" %(num,chr(num)))

#list使用练习,声明一个list类型的变量classmates
classmates = ['wang','guo','ren']

#将指定元素添加到list变量的指定位置中 insert方法参数分别为添加的位置以及添加的内容

#向list变量中添加新变量,并且该变量为原list变量的第一个参数
classmates.insert(0,'Li')

#向list变量中添加新变量,并且该变量为原list变量的最后一个参数
#classmates.insert(len(classmates),'Ma')
classmates.append('Ma')

#以下三行为打印list变量整体内容以及打印list变量指定域的内容
#print("list classmates is :%s" %(classmates))
#print("the first elements is :%s" %(classmates[0]))
#print("the last elements is :%s" %(classmates[-1]))

#可以使用pop方法删除list变量中的元素 pop(i),i为要删除元素的索引位置
#classmates.pop(-1)	#删除最后一个元素
#print(classmates)

#如果要把list中的元素替换为其他元素,可以直接给对应元素赋值
#classmates[0] = 'Zhai'
#print(classmates)

#list里面元素的数据类型可以不同,如下面变量
#List = ['guoguo',1987,True]
#print("the new list is %s" %(List))

#list中的元素可以是另外一个list
#s = ['python','java',['asp','php'],'scheme']
#print("the list emel s is:%s" %(s))
#print("len(s) = %d " %(len(s)))

#tuple数据类型和list类似,但是tuple一旦初始化就不能被修改,注意,list定义时使用的是方括号,而tuple定义时使用的为圆括号
#classmate = ('123','456')
#print(classmate)

#如果tuple类型的变量只需要有一个整数值,不可以赋值为(1),而应该赋值为(1,)

#练习
L = [
		['Apple', 'Google', 'Microsoft'],
		['Java', 'Python', 'Ruby', 'PHP'],
		['Adam', 'Bart', 'Lisa']
	]

#打印Apple
#print(L[0][0])

#打印Python
#print(L[1][1])

#打印Lisa
#print(L[2][2])

#条件判断练习
#age = 6 
#if(age > 18):
#	print("Your age is :%d" %age)
#	print("adult")
#elif(age >= 6):
#	print("Your age is :%d" %age)
#	print("teenager")
#else:
#	print("Your age is :%d" %age)
#	print("kid")
#
#s = input('birth:')
#
#if(int(s) < 2000):
#	print('00前')
#else:
#	print('00后')


#循环,for...in循环
#names = ['Michael', 'Bob', 'Tracy']
#for name in names:
#	print(name)

#计算1到10整数的总和
#sum = 0
#for i in [1,2,3,4,5,6,7,8,9,10]:
#	sum = sum + i
#print(sum)

#在上例中,整数范围可以使用range()函数生成一个整数序列,再通过list()函数转换为list,
#如range(5)生成的为从0开始小于5的整数
#print(list(range(5)))

#while循环
#sum = 0
#n = 99
#while(n >= 0):
#	sum = sum + n
#	if(n <= 50):
#		break
#	n = n-2

#print("n = %d,sum = %d" %(n,sum))


#dict为python内置字典,相当于java中的map存储的为键-值对,声明dict使用大括号{}\
#一个key只能对应一个value,如果多次对一个key赋值,后面的值会把前面的值冲掉
d = {'Michael':95,'Bob':75,'Tracy':85,"James":100}
print(d)
d['Tracy'] = 100
print(d['Tracy'])

#如果key不存在,则dict会报错,有两种方法避免key不存在的情况
name = 'Tomas'
#1 通过in判断key是否存在：
print('if %s in dict? %s' %(name,name in d))

name = 'Michael'
print('if %s in dict? %s' %(name,name in d))

#2 通过dict提供的get方法,如果key不存在,可以返回None,或者自己指定的value
print(d.get('Tomas'))	#get方法如果键不存在,默认返回None
print(d.get('Tomas',-1))	#为get方法添加不存在时返回的value,value可以为数值也可以为字符串

#删除一个key,可以使用pop方法,pop(key),如果pop中key值不存在,则会报错
d.pop('Michael')
print(d)

#数据类型转换

#int()将其他类型数据转换为整型数据
print('int(\'123\') = %d,int(12.34) = %d' %(int('123'),int(12.34)))

#float()将其他类型数据转换为浮点型
print('float(12) = %.2f float(\'1234.31\') = %.2f' %(float(12),float('1234.31')))

#str()将其他类型数据转换为字符串
print('str(100) = %s' %(str(100)))

#bool()将其他类型数据转换为布尔型

#参数检查,参数检查使用内置函数isinstance()实现,下面代码检查x是否是int或float类型的值
x = 4
print(isinstance(x,(int,float)))

x = 5.11
print(isinstance(x,(int,float)))

x = 'abc'
print(isinstance(x,(int,float)))


#定义函数
#在python中,定义一个函数要使用def关键字,依次写出函数名、括号、括号中的参数和冒号:,在缩进块儿中编写函数体,函数的返回值用return语句返回
def my_abs(x):
	
	#判断传入的值是否是整型或者浮点型
	if(not(isinstance(x,(int,float)))):
		print("input number is invalid")
		return -1
	
	if(x > 0):
		return x
	else:
		return -x

#定义空函数
def void_func():
	pass

#调用上面定义的my_abs函数
#print('my_abs(-1) = %d' %(my_abs(-1)))

#返回多个值的函数
