#!/usr/bin/python3.5

######################################################
##	文件名:		io_test.py
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

write_test()