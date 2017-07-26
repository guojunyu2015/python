#!/usr/bin/python3.5
import socket
import time
import datetime

#IP地址及端口号
ip_addr = '127.0.0.1'
port_no = 8000 

timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')

tran_list = (1,2,3)
tran_type = int(input('请选择交易类型:\n\t1-缴费查询\n\t2-缴费\n\t3-对账\n'))

if tran_type not in tran_list:
	raise ValueError('bad select')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#建立连接
s.connect((ip_addr,port_no))

#发送数据
#如果为缴费查询
if tran_type == 1:
	str_tmp = '0001#1501#150000#%s#user_id#0000#%s#1####' %(timestamp,timestamp)
elif tran_type == 2:
	str_tmp = '0002#1501#150000#%s#66229302#zhanghao#100#user_id#1######' %timestamp
else:
	str_tmp = '0007#1501#150000#%s#100#1#DZ_150000050001_105110_20170312_00001.V#########' %timestamp

#封装整体报文(添加报文长度)
send_msg = '%06d#%s' %(len(str_tmp)+7,str_tmp)

print('发送信息:[%s]' %send_msg)

#发送数据
s.send(send_msg.encode('gbk'))

#接收应答数据,应答数据存储在list变量中.
buffer = []

while True:
	d = s.recv(1024)
	if d:
		buffer.append(d)
	else:
		break

#调用bytes类的join方法将list变量中的bytes内容保存到rcv_str中
rcv_str = b''.join(buffer)
print('应答信息:[%s]' %(rcv_str.decode('utf-8')))

s.close()
