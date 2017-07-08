#!/usr/bin/python3.5

######################################################
##	文件名:		object.py
##	文件说明:	python面向对象练习,所有相关知识点均封装在函数中,调用函数来练习
##	创建时间:	2017年7月7日13:28:55
######################################################


def class_basic():
	#声明一个类Student,括号中的object指的是Student类继承的类,object类是所有类的父类
	class Student(object):
		pass
	
	bart = Student()
	#在python中,类的对象可以随意使用任何属性,例如下面可以使用name属性
	bart.name = 'Kobe'
	print(bart)

#class_basic()

def class_basic_1():
	class Student(object):
		#__init__函数为类的构造函数,构造函数名固定为__init__,而类的所有方法的第一个参数必须为self,
		#该参数在调用方法时不需要传递,类似于this指针,后面的name和score则必须传递
		def __init__(self,name = 'Default',score = 60):
			self.name = name
			self.score = score
		
		def print_score(self):
			print('%s:%s' %(self.name,self.score))
		
		def get_score(self):
			if self.score >= 90:
				return 'A'
			elif self.score >= 60:
				return 'B'
			else:
				return 'C'
			
			
	bart = Student('Kobe',90)
	bart1 = Student()
	
	bart.print_score()
	bart1.print_score()
	
	print(bart.get_score())
	print(bart1.get_score())

#class_basic_1()

def class_limit():
	#类的访问权限控制
	class Student(object):
		def __init__(self,name,score):
			#在下面两行代码中,变量名前面加__表示变量为私有变量,只能在类中被访问,无法在类外面被访问
			self.__name = name
			self.__score = score
		
		def print_score(self):
			print('%s:%s' %(self.__name,self.__score))
	
	bart = Student('Bart Simpson', '98')
	bart.print_score()
	

#class_limit()

def class_sub():
	
	#关于继承和多态的练习,Animal为基类
	class Animal(object):
		def run(self):
			print('Animal is running...')
	
	#定义Dog类从Animal类继承
	class Dog(Animal):
		def run(self):
			print('Dog is running...')
	
	#定义Cat类从Animal类继承
	class Cat(Animal):
		def run(self):
			print('Cat is running...')
	
	dog = Dog()
	dog.run()
	
	cat = Cat()
	cat.run()
	
	print(isinstance(dog,Animal),isinstance(dog,Dog))
	
	#多态函数测试,相当于java中的父类引用指向子类的对象,调用run_time函数时,如果传入的是
	#animal对象,调用animal类的run方法,传入的为animal子类的对象,则调用animal子类的run方法
	def run_time(animal):
		animal.run()
		animal.run()
	
	run_time(dog)
	run_time(cat)
	animal = Animal()
	run_time(animal)

class_sub()