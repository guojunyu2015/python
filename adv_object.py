#!/usr/bin/python3.5
from types import MethodType
######################################################
##	文件名:		adv_object.py
##	文件说明:	python高级面向对象练习,所有相关知识点均封装在函数中,调用函数来练习
##	创建时间:	2017年7月11日08:51:31
######################################################

def obj_test():
	class Student(object):
		pass
	s = Student()
	s.name = 'Michael'	#动态给实例绑定一个属性
	
	#也可以动态的给实例绑定一个方法
	def set_age(self,age):
		self.age = age
	
	s.set_age = MethodType(set_age,s)	#给实例绑定一个方法
	s.set_age(25)
	print(s.age)
	
	#给对象s绑定的方法set_age,对该类的其他对象是无效的.
	s1 = Student()
	
	#以下语句错误,s1不可以调用set_age方法
	#s1.set_age(10)	
	
	#如果想要给所有的实例都绑定方法,可以给class绑定方法
	def set_score(self,score):
		self.score = score
	
	Student.set_score = set_score	#给student类绑定方法,绑定之后,所有Student类的对象都可以使用该方法
	s2 = Student()
	s2.set_score(100)
	print(s2.score)
	
#obj_test()

def slots_test():
	#在上面的函数中,类定义好以后仍旧可以给类对象添加属性和方法,如果想要限制实例的属性,
	#比如只允许对Student类添加name和age属性,可以通过__slots__特殊变量来限制该class能添加的属性
	class Student(object):
		__slots__ = ('name','age')	#用tuple定义允许绑定的属性名称
		
	s = Student()
	s.name = 'Michael'	#绑定属性name
	s.age = 24			#绑定属性age
	#s.score = 100		#绑定属性score,该语句错误,不可以绑定属性score
	
	print(s.name,s.age)
	#注:slots属性只对当前类有效,对于其子类是无效的
	
#slots_test()

def property_test():
	#在上面的例子中,Student类的score属性可以设置任意值,但是score的合理范围为整数,数值范围为0到100
	#可以通过get_score和set_score两个函数来操作score的值,对其加以控制
	
	#python内置的
	class Student(object):
		
		def get_score(self):
			return self.score
		
		def set_score(self,score):
			if not isinstance(score,int):
				print('score must be an integer!')
				return -1
			if score < 0 or score > 100:
				print('score must between 0 and 100')
				return -1
			self.score = score
		
	s = Student()
	s.set_score(100)
	print(s.get_score())

property_test()		