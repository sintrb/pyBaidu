# -*- coding: UTF-8 -*
'''
Created on 2013-10-14

@author: RobinTang
'''


import time
from HttpHolder import HttpHolder


import sys
try:
	sys.setdefaultencoding("utf-8")
except:
	pass


def strbetween(s, ss, es):
	si = s.index(ss)
	return s[si:s.index(es, si)]

class BaseBaiduUser():
	'''
	基础百度用户
	'''
	def __init__(self, cookies):
		'''
		创建一个BaseBaiduUser实例，需指定可用的Cookie，主要是BDUSS值
		'''
		self.http = HttpHolder(headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.57 Safari/537.36'})
		self.http.set_cookiesdict(cookies)

	def verifyCookie(self):
		'''
		检查当前Cookie是否可用
		'''
		url = 'http://i.baidu.com/center'
		self.http.open_html('http://i.baidu.com/center')
		return self.http.geturl() == url
	
	def sendMessage(self, touser, message='message'):
		'''
		发送消息
		touser, 消息目的用户名
		message, 消息内容
		'''
		form = {
			'msgcontent':message,
			'msgreceiver':touser,
			'refmid':'5255694744',
			'vcode':'',
			'msgvcode':'',
			'bdstoken':'7e1fee8373e8883e95da301f7d2194ec',
			'qing_request_source':''
			}
		head = {
			'Origin':'http://msg.baidu.com',
			'Referer':'http://msg.baidu.com/?t=%d' % (time.time() - 100),
			'X-Requested-With':'XMLHttpRequest'
			}
		html = self.http.open_html(url='http://msg.baidu.com/msg/writing/submit/msg', headers=head, data=form)
		return html.find('errorNo : "0"') >= 0
	
	def createText(self, title='Title', content='Content'):
		form = {
			'title':title,
			'content':'<p>%s</p>' % content,
			'private':'',
			'imgnum':'0',
			'bdstoken':'7e1fee8373e8883e95da301f7d2194ec',
			'qbid':'',
			'refer:http':'//hi.baidu.com/home/?from=index',
			'multimedia[]':'',
			'synflag':'',
			'private1':'',
			'qing_request_source':'new_request'
			}
		head = {
			'Origin':'http://hi.baidu.com',
			'Referer':'http://hi.baidu.com/pub/show/createtext',
			'X-Requested-With':'XMLHttpRequest'
			}
		html = self.http.open_html(url='http://hi.baidu.com/pub/submit/createtext', headers=head, data=form)
		return html.find('"errorNo" : "0"') >= 0
		
if __name__ == '__main__':
	import config
	# cookies值现在测试出来只需要BDUSS即可
	bdu = BaseBaiduUser(cookies=config.baiducookie)
	
	# 验证Cookie是否可以使用
	if bdu.verifyCookie():
		# 发私信消息
		print bdu.sendMessage(touser='trbbadboy', message='小道消息:%d' % time.time())
		
		# 在百度空间创建文章
		print bdu.createText(title='标题%d' % time.time(), content='内容啊内容%d' % time.time())
	

