# -*- coding: UTF-8 -*
'''
Created on 2013-10-14

@author: RobinTang
'''

import re
import config
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
	def __init__(self, username=None, password=None, cookies=None):
		'''
		创建一个BaseBaiduUser实例，可以指定拜user中Http请求的最初Cookie
		'''
		self.http = HttpHolder(headers={'User-Agent':'"Mozilla/5.0 (Windows NT 6.1; rv:24.0) Gecko/20100101 Firefox/24.0"'})
		self.username = username
		self.password = password
		if cookies:
			self.http.set_cookiesdict(cookies)

	def login(self):
		'''
		用户登陆
		'''
		html = self.http.open_html('http://wappass.baidu.com/passport')
		fhtml = strbetween(html, '<form action="/passport/login" method="post">', '</form>')
		form = dict(re.findall('<input type="hidden".*name="(.*)"\s*value="(.*)"[\s/]*>', fhtml, re.IGNORECASE | re.MULTILINE))
		form['username'] = self.username
		form['password'] = self.password
		form['submit'] = '登录'
		html = self.http.open_html('http://wappass.baidu.com/passport/login', headers={'Referer': 'http://wappass.baidu.com/passport?login'}, data=form)
		checkstr = '%s'%self.username
		html = self.http.open_html('http://tieba.baidu.com/')
		return html.find(self.username)>=0
		
if __name__ == '__main__':
	bdu = BaseBaiduUser(config.username, config.password)
	print bdu.login()
	

