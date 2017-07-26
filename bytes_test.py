#!/usr/bin/python3.5

#bytes数据类型测试
a = '中文'
print('len(a) = %d' %len(a))

#如果需要测试str类型所占用的字节数,需要将str类型转换为bytes类型后,获取bytes类型数据的长度
b = a.encode('utf-8')
print('isinstance(b,list)',isinstance(b,list))
print('len(b) = %d' %len(b))
print(a,b)
print(b.decode())

c = b'ddd'
c.join(b'aaa')
print(isinstance(c,bytes))
print(c)

d = []
print(isinstance(d,list))