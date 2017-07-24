#!/usr/bin/python3.5

######################################################
##	文件名:		func_python.py
##	文件说明:	python函数式编程练习,所有相关知识点均封装在函数中,调用函数来练习
##	创建时间:	2017年7月14日12:54:293
######################################################

def test():
	num = -10
	print(abs(num))
	
	#函数名称也是变量,可以把函数名称赋值给变量,再通过变量调用该函数
	func = abs
	print(func(num))


#test()

def high_order():
	#高阶函数练习,高阶函数指的是将函数名称当做参数传递给另外一个函数
	def add(x,y,f):
		return f(x) + f(y)
	
	#调用add函数,f参数传递为abs
	num = add(-5,-6,abs)
	print(num)	#输出值为11

#high_order()

def map_test():
	#python内建了map和reduce函数,map函数接收两个参数,一个是函数,一个是Iterable,map将传入的函数依次作用到
	#序列的每个元素,并把结果作为新的Iterable返回.
	
	#假设有函数 f(x) = x平方值,要把这个函数作用在一个list上,可以用map()实现如下:
	def f(x):
		if(isinstance(x,int)):
			return x * x
		else:
			return -1
	
	l = list(range(1,10))
	print(l)
	ll = list(map(f,l))
	print(ll)
	
#map_test()

from functools import reduce
def reduce_test():
	#reduce把一个函数作用在一个list上,这个函数必须接收两个参数,reduce把结果继续和序列的下一个元素
	#做累积计算,其效果就是
	#reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
	#reduce返回的为一个值
	def add(x,y):
		return x + y
	
	l = list(range(1,11))
	print(l)
	
	sum_val = reduce(add,l)
	print(sum_val)
	
	#将[1,2,3,4,5]转换为整数12345
	def fn(x,y):
		return x * 10 + y
	
	l = list(range(1,6))
	val = reduce(fn,l)
	print(val)
	
reduce_test()

