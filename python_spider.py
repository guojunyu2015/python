#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup
import re
import time
import sys
import os

max_count = 9999

#该工具用于从笔趣阁网站爬取小说,笔趣阁网站小说首页:http://www.biqukan.com/
src_url = "http://www.biquge5200.com/"

#小说名称可以自动从url中截取
url = "http://www.biquge5200.com/1_1273/"

#小说文件名截取url中最后的数字值
file_name = url[len(src_url):url.rfind('/')] + '.txt'

r = requests.get(url)
#遍历所有的章节链接
soup = BeautifulSoup(r.text, 'html.parser')

title_name = soup.find('meta',{'property':'og:title'}).get('content')
novel_name = title_name
print('小说名称:',novel_name,'文件名称:',file_name)

file_exist_flag = os.path.exists('./%s' %file_name)

#目标文件第二行保存当前文件中的章节总数
if(file_exist_flag == False):
	fp = open(file_name,'w+')
	fp.write('当前章节总数:[00000]'+'\n')
	fp.write(novel_name + '\n')
	curr_section_num = 0
else:
	fp = open(file_name,'a+')
	fp.seek(0,0)
	line = fp.readline()
	#从文件第一行获取当前章节总数
	curr_section_num = int(line[line.index('[')+1:line.index(']')])
	print('当前章节总数:',curr_section_num)
	fp.seek(0,2)
#遍历章节列表标签,依次截取章节地址以及章节名称
bgn_flag = False
sum_section_count = 0
section_name_list = []
section_addr_list = []
for section_addr in soup.find_all(re.compile(u'd[d,t]')):
	if(section_addr.name == 'dt' and '正文' in section_addr.get_text() and novel_name in section_addr.get_text()):
		bgn_flag = True
		continue
	
	if(bgn_flag == True):
		#解析章节的地址
		dtl_addr = section_addr.a.get('href')
		dtl_name_str = section_addr.a.string.replace('(','（')
		if(dtl_name_str.find('（') > 0):
			dtl_name = dtl_name_str[0:dtl_name_str.find('（')]
		else:
			dtl_name = dtl_name_str
		section_name_list.append(dtl_name)
		section_addr_list.append(dtl_addr)
		sum_section_count = sum_section_count + 1
		if(sum_section_count >= max_count):
			break

if(sum_section_count <= curr_section_num):
	print('小说<<%s>>当前章节为最新章节,无需更新' %novel_name)
	exit()
else:
	print('小说<<%s>>最新章节为%d,当前文件中最新章节为%d,需要更新的章节数%d' %(novel_name,sum_section_count,curr_section_num,sum_section_count-curr_section_num))

print("<<%s>>下载中" %(novel_name))

i = curr_section_num
while i < sum_section_count:
	#解析章节的地址
	dtl_addr = section_addr_list[i]
	dtl_name = section_name_list[i]
	fp.write(dtl_name + '\n')
	r1 = requests.get(dtl_addr)
	novel_soup = BeautifulSoup(r1.text, 'html.parser')
	novel_text_soup = novel_soup.find('div',{'id':'content'})
	if(novel_text_soup.get_text() == None):
		print('章节名称:',dtl_name,'内容为空')
	novel_text = novel_text_soup.get_text().replace('　　','\n')
	fp.write(novel_text + '\n')
	
	sys.stdout.write("已下载:%.1f%%" %  float(i/sum_section_count * 100) + '\r')
	sys.stdout.flush()
	time.sleep(0.5)
	i += 1
fp.close()

#下载结束,将最新章节总数写入到文件中
fp = open(file_name,'r+')
fp.seek(0)
fp.write('当前章节总数:[%05d]' %sum_section_count)
fp.close()
print('<<%s>>下载结束,下载章节总数:%d' %(novel_name,sum_section_count-curr_section_num))