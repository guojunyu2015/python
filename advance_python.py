#!/usr/bin/python3.5
from collections import Iterable

######################################################
##	文件名:		advance_python.py
##	文件说明:	python高级特性练习
##	创建时间:	2017年7月6日12:30:29
######################################################

#切片(Slice),指从list和tuple取出部分值的方法
def slice_test1():
	L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
	print('list L = ',L)
	
	#取list L的前3个元素 L[0:3]表示从L的下标0开始取值,一直到下标3,但是不包括下标3
	print('L的前三个元素为',L[0:3])
	
	print('L的第二个和第三个元素为',L[1:3])
	
	print('L从第二个元素开始到最后一个元素为',L[1:])
	
	print('L从倒数第二个元素开始到最后一个元素为',L[-2:])
	
	print('L的前三个元素为',L[:3])

def slice_test2():
	number = list(range(20))
	print('number = ',number[:])
	print('取number的前10个数',number[:10])
	print('取number的前10个数,每两个取一个',number[:10:2])
	print('取number的所有数,每五个取一个',number[::5])


#tuple的切片操作和list类似,只是tuple的切片结果仍旧是tuple,值不可变
#slice_test2()

#迭代(Iteration),如果给定一个list或tuple,可以通过for循环来遍历这个list或tuple,这种遍历我们成为迭代
#在python中,迭代是通过for.....in来完成的

def iterator_test():
	#迭代测试
	
	#迭代list
	print('开始进行list迭代测试')
	L = list(range(10))
	for i in L:
		print (i)
	print('list迭代测试结束')
	
	#迭代dict(默认迭代dict的key)
	print('开始进行dict迭代测试')
	L = {'a':1,'b':2,'c':3}
	for i in L:
		print(i)
	print('dict迭代测试结束')
	
	#迭代dict的value
	print('开始进行dict的value迭代测试')
	for i in L.values():
		print(i)
	print('dict的value迭代测试结束')
	
	#同时迭代dict的key和value
	print('开始进行dict的key和value同时迭代测试')
	for i in L.items():
		print(i)
	print('dict的key和value同时迭代测试结束')
	
	#判断一个对象是否可以迭代,通过collections模块的Iterable类型判断\
	print('字符串是否可以迭代',isinstance('abc', Iterable))		#判断字符串是否可以迭代
	print('字符串是否可以迭代',isinstance([1,2,3], Iterable))	#判断list是否可以迭代
	print('整数是否可以迭代',isinstance(11, Iterable))			#判断整数是否可以迭代

#iterator_test()

#列表生成式(List comprehensions),是Python内置的可以用来创建list的生成式
def list_comprehen():
	
	#要生成list[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],可以用如下方式
	L = list(range(1,11))
	print(L)
	
	#生成list [1x1, 2x2, 3x3, ..., 10x10],可以用循环,也可以用
	#使用循环生成
	L = []
	for i in list(range(1,11)):
		L.append(i * i)
	print(L)
	
	#使用列表生成式生成1-10平方值的list
	L = [x * x for x in range(1,11)]
	print(L)
	
	#使用列表生成式生成1-10中偶数平方值的list,for循环后面可以使用if判断语句
	L = [x * x for x in range(1,11) if x % 2 == 0]
	print(L)
	
	#可以使用两层循环,生成全排列
	L = [m+n for m in 'ABC' for n in 'XYZ']
	print(L)
	
#list_comprehen()

#生成器(generator),生成器为相对于列表而言的,列表创建后会将所有元素都在内存分配空间,如果列表容量过大,
#会造成内存浪费,生成器为动态根据列表的规则生成列表值的方法,声明时只要将方括号修改为圆括号即可

def generator_test():
	
	#用生成式生成列表L,L的值为1到10
	L = [x * x for x in range(1,11)]
	print(L)
	
	#用生成器生成列表,此时列表值无法直接打印出来
	L = (x * x for x in range(1,11))
	print(L)
	
	for i in L:
		print(i)

generator_test()
