# -*- coding: UTF-8 -*
'''
Created on 2013-10-14

@author: RobinTang
'''

import re

from HttpHolder import HttpHolder

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
# 		print self.http.get_cookiesdict()
		fhtml = strbetween(html, '<form action="/passport/login" method="post">', '</form>')
		form = dict(re.findall('<input type="hidden".*name="(.*)"\s*value="(.*)"[\s/]*>', fhtml, re.IGNORECASE | re.MULTILINE))
		form['username'] = self.username
		form['password'] = self.password
		form['submit'] = '{U'
		print form['vcodestr']
# 		print form
		html = self.http.open_html('http://wappass.baidu.com/passport/login', headers={'Referer': 'http://wappass.baidu.com/passport?login'}, data=form)
		fhtml = strbetween(html, '/passport/login', '</form>')
		form = dict(re.findall('<input type="hidden".*name="(.*)"\s*value="(.*)"[\s/]*>', fhtml, re.IGNORECASE | re.MULTILINE))
		print form['vcodestr']
		
if __name__ == '__main__':
	bdu = BaseBaiduUser('username', 'password')
	print bdu.login()
	

