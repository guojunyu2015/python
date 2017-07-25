#!/usr/bin/python3.5

######################################################
##	文件名:		debug_test.py
##	文件说明:	python错误调试
##	创建时间:	2017年7月18日22:09:573
######################################################

def try_test():
	try:
		print('try...')
		r = 10 / 2
		print('result:',r)
	except ZeroDivisionError as e:
		print('except:',e)
	
	finally:
		print('finally...')
	print('End')

#try_test()

import logging
def foo(s):
	return 10/int(s)

def bar(s):
	return foo(s) * 2

def main():
	try:
		bar('0')
	except Exception as e:
		logging.exception(e)
	
	print('End')

main()