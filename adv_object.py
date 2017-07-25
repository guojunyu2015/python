#!/usr/bin/python3.5

######################################################
##	文件名:		adv_object.py
##	文件说明:	python高级面向对象练习,所有相关知识点均封装在函数中,调用函数来练习
##	创建时间:	2017年7月13日21:42:22
######################################################

def dyna_block():
	#动态绑定属性及方法练习,给一个实例绑定属性可以直接使用,可以给一个具体对象绑定方法,也可以给类绑定方法
	
	class Student(object):
		pass
	
	s = Student()
	s.name = 'Michael'	#动态的为实例s绑定name属性
	print(s.name)
	
	#也可以动态的为实例绑定一个方法
	def set_age(self,age):
		self.age = age
	
	from types import MethodType
	
	#将方法set_age绑定到实例s上
	s.set_age = MethodType(set_age,s)
	s.set_age(25)
	print(s.age)
	
	#以上给实例s绑定的方法set_age,对于Student类的其他对象是不起作用的
	s2 = Student()
	#s2.set_age(25)	#错误的调用
	
	#如果想让Student类的所有实例都使用方法,可以给类绑定方法
	def set_score(self,score):
		self.score = score
	
	Student.set_score = set_score
	
	s2.set_score(80)
	print(s2.score)

#dyna_block()

def slots_test():
	#slots练习,如果想要限制实例的属性,例如只允许对Student类的实例添加name和age属性。
	#定义类的时候,可以定义一个特殊的__slots__变量
	class Student(object):
		__slots__ = ('name','age')	#赋值为一个tuple类型的变量
	
	s = Student()
	s.name = 'Michael'
	s.age = 25
#	s.score = 100	#错误,不能绑定score属性
	print('name = ',s.name,'age = ',s.age)
	
	#注:__slots__定义的属性仅对当前类的实例其作用,对继承的子类是不起作用的
	
#slots_test()

def multi_test():
	#多重继承测试
	#第一层为动物类,第二层为哺乳类和鸟类
	class Animal(object):
		pass
	
	#哺乳类
	class Mammal(Animal):
		pass
	
	#鸟类
	class Bird(Animal):
		pass
	
	#各种动物
	class Dog(Mammal):
		pass
	
	class Bat(Mammal):
		pass
	
	class Parrot(Bird):
		pass
	
	class Ostrich(Bird):
		pass
	
	#接下来给动物添加Runnable和Flyable的功能,只需要先定义好Runnable和Flyable的类
	class Runnable(object):
		def run(self):
			print('Running...')
	
	class Flyable(object):
		def fly(self):
			print('Flying...')
	
	#对于需要Runnable功能的动物,就多继承一个Runnable,例如Dog类
	class Dog(Mammal,Runnable):
		pass
	
	#对于需要Flyable功能的动物,就多继承一个Flyable,例如Bat
	class Bat(Mammal,Flyable):
		pass
	
	#MixIn在设计类的继承关系时,通常,主线都是单一继承下来的,例如,Ostrich继承自Bird。但是,如果需要“混入”额外的功能,
	#通过多重继承就可以实现,比如,让Ostrich除了继承自Bird外,再同时继承Runnable。这种设计通常称之为MixIn
	#MinIn的目的就是给一个类增加多个功能.

def cust_made():
	#本函数为定制类测试
	
	#__str__定制类
	class Student(object):
		def __init__(self,name):
			self.name = name
		
		def __str__(self):
			return 'Student object(name:%s)' %(self.name)
		
		def __repr__(self):
			return 'Student object(name:%s)' %(self.name)
		
	print(Student('Michael'))	#输出为:Student object(name:Michael),print调用的为类的__str__方法
	
	s = Student('Jamas')
	s					#此时调用的为__repr__()方法,如果类中未声明,则无输出,__repr__()的内容和__str__一般相同
	
	#__iter__,如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法
	class Fib(object):
		def __init__(self):
			self.a,self.b = 0,1
			
		def __iter__(self):
			return self
		
		def __next__(self):
			self.a, self.b = self.b, self.a + self.b
			
			if self.a > 10:
				raise StopIteration()
			return self.a
#	for i in Fib():
#		print(i)
	
	#__getitem__,Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行，比如，取第5个元素,Fib(5)
	
	
	#__getattr__,正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错。要避免这个错误,那就是写一个__getattr__()方法，动态返回一个属性
	class Student(object):
		def __init__(self):
			self.name = 'Michael'
		
		def __getattr__(self,attr):
			if attr == 'score':
				return 99
	
	s = Student()
	print(s.score)		#Student类中兵没有score属性,Python解释器会试图调用__getattr__(self, 'score')来获取属性.
	print(s.age)		#Student类中没有age属性,__getattr__方法中也没有,输出为NULL
	
cust_made()