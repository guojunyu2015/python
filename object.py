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
	
	#以下语句会运行错误,私有变量无法在外部直接访问
	#print(bart.__name)
	
	#以下语句运行会通过,但是并不是给Student对象中的__name属性赋值,因为python在类外部会将私有变量修改为_Student__name,以下语句
	#相当于给对象bart新增了一个__name属性,和结构体中的私有变量不是一个变量,通过下面的两次打印处理可以看出区别
	bart.__name = '123'
	print(bart.__name)
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

#class_sub()


def get_object_info():
	#获取对象信息,即根据对象判断对象的类型以及这个对象有哪些方法
	
	#使用type函数判断
	print(type(123))		#输出为:<class 'int'>
	print(type('123'))		#输出为:<class 'str'>
	print(type(12.1))		#输出为:<class 'float'>
	
	print(type(123)==int)	#输出为:True
	print(type('123')==str)	#输出为:True
	
	#使用type函数判断一个对象是否是函数
	import types
	def fn():
		pass
	
	print(type(fn) == types.FunctionType)	#types.FunctionType为常量,输出为True
	print(type(abs)==types.BuiltinFunctionType)
	
	#使用isinstance()函数,在上面的函数中已经有练习
	
	#使用dir()函数,dir函数可以获得一个对象所有的属性和方法
	
	#获取str对象的所有属性和方法
#	print(dir('123'))
	
	
#get_object_info()


def set_object_attr():
	#dir函数配合getattr(),setattr(),hasattr()可以直接操作一个对象的状态
	class MyObject(object):
		
		def __init__(self):
			self.x = 9
		
		def power(self):
			return self.x * self.x
	
	obj = MyObject()
	
	#测试obj对象有没有x属性
	print(hasattr(obj,'x'))		#输出为True
	print(getattr(obj,'x'))		#获取属性x,输出为9
	
	#测试obj对象有没有y属性
	print(hasattr(obj,'y'))		#输出为False
	setattr(obj,'y',19)			#新增属性y,值为19
	print(getattr(obj,'y'))
	
	print(obj.y)				#输出为19,属性y已经添加成功
	
	#判断对象是否有power方法
	print(hasattr(obj, 'power'))	#输出为True
	
	#获取方法power
	print(getattr(obj, 'power'))
	
	fn = getattr(obj, 'power') # 获取属性'power'并赋值到变量fn
	print(fn())	#输出为81
	
#set_object_attr()

def instance_attr():
	#实例属性和类属性,以下面的类定义为例
	class Student(object):
		name = 'Name'		#name为类属性,归Student类所有,类的所有实例都可以访问到
		def __init__(self,job):
			self.job = job
	
	s = Student('study')
	s.score = 90
	
	#在上面的类定义和实例化中,对象s有两个属性,一个为在类定义中通过self生成的属性job,另外一个为实例自身新增的属性score,
	#而job属性则为类定义
	
	print(s.name)			#打印name属性,因为实例并没有name属性,所以会继续查找class的name属性
	print(Student.name)		#打印类的name属性
	
	s.name = 'Michael'		#给实例绑定name属性
	print(s.name)			#由于实例属性优先级比类属性高,因此,它会屏蔽掉类的name属性,输出为Michael,而不是Name
	
	del s.name				#如果删除实例的name属性
	print(s.name)			#再次调用s.name,由于实例的name属性没有找到,类的name属性就显示出来了
	
instance_attr()
	
	
		