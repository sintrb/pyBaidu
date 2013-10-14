# -*- coding: UTF-8 -*
'''
Created on 2013-10-14

@author: RobinTang
'''

from HttpHolder import HttpHolder

class BaseBaiduUser():
	'''
	基础百度用户
	'''
	def __init__(self, cookies=None):
		'''
		创建一个BaseBaiduUser实例，可以指定拜user中Http请求的最初Cookie
		'''
		self.http = HttpHolder()
		if cookies:
			self.http.set_cookiesdict(cookies)


if __name__ == '__main__':
	pass

