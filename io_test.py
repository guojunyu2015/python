#!/usr/bin/python3.5

######################################################
##	文件名:		io_test.py
<<<<<<< HEAD
##	文件说明:	python IO练习,所有相关知识点均封装在函数中,调用函数来练习
##	创建时间:	2017年7月20日09:42:48
######################################################

def read_test():
#	f = open('./file/test.txt')
#	print(f.read())
#	f.close()
	
	#with操作包含了打开和关闭文件的操作,open方法中的第二个参数r表示以文本形式打开文件,
	#如果需要以二进制方式打开文件,使用rb即可
#	with open('./file/test.txt','r') as f:
		#print(f.read())	#read方法读取文件的全部内容
		
		#逐行读取文件内容
#		for line in f.readlines():
#			print(line.strip())		#strip方法用于去掉末尾的换行符
	
	#以二进制方式打开文件
#	with open('./file/test.txt','rb') as f:
#		for line in f.readlines():
#			print(line.strip())
	
	#python默认以UTF-8的编码格式读取文件,如果需要按指定格式打开文件
	f = open('./file/test.txt','r',encoding='gbk')
	print(f.read())
	f.close()
	
	
#read_test()

def write_test():
	with open('./file/write_test.txt','w') as f:
		f.write('Hello,world')

#write_test()

def stringio_test():
	#StringIO只能操作str
	from io import StringIO 
	f = StringIO()
	f.write('hello')
	f.write(' ')
	f.write('world')
	print(f.getvalue())		#getvalue函数用于
	
#stringio_test()

def byteio_test():
	from io import BytesIO
	f = BytesIO()
	f.write('中文'.encode('utf-8'))
	
	print(f.getvalue())

#byteio_test()

import os
def environ_test():
	
	#获取操作系统类型,如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统.
	print(os.name)
	
	#获取操作系统详细信息
	print(os.uname())
	
	#操作系统的全部环境变量保存在os.environ变量中
	print(os.environ)
	
	#获取某个环境变量的值,可以调用os.environ.get('key')
	print(os.environ.get('HOME'))
	print(os.environ['HOME'])
	
#environ_test()

def dir_test():
	#操作文件和目录,操作文件和目录的函数一部分放在os模块中,一部分放在os.path模块中
	
	#查看当前目录的绝对路径
	print(os.path.abspath('.'))
	
	#将两个路径合并为一个路径,使用此函数是为了应对不通操作系统的情况
	union_path = os.path.join(os.path.abspath('.'),'testdir')
	print(union_path)
	
	#拆分路径,第二部分为最后一级的文件或目录或文件名
	print(os.path.split(union_path))
	
	#获取文件扩展名
	print(os.path.splitext('/home/guoguo/github/python/io_test.py'))
	
	#创建新目录
#	os.mkdir('./testdir')
	
	#删除目录
#	os.rmdir('./testdir')
	
#dir_test()

#序列化测试,将内存中的变量内容保存到磁盘上(pickling)以及从磁盘上获取内容(unpickling)
import pickle

def pick_test():
	d = dict{name = 'Michael',age = 20,score = 100}
	
	pickle.dumps(d)
=======
##	文件说明:	pythonIO操作练习
##	创建时间:	2017年7月18日22:09:573
######################################################

def read_file():
	f = open("test.txt",'r')
	str = f.read()	#read方法为一次读取文件的全部内容
	print(str)
	f.close()
	
read_file()
>>>>>>> dc1dc5cb6ba0963d270a52023fdaf001ff5a38e7
