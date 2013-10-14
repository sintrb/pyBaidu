# -*- coding: UTF-8 -*
'''
Created on 2013-10-14
HTTP请求保持
@author: RobinTang
'''

import urllib2
import cookielib
import types
import re

def urlencode(param):
	'''
	正如你所理解的URLEncode一样。
	接受字符串和字典两种类型，字典类型在Encode之后键值对(key=value)之间用&连接，字符串直接Encode
	'''
	if type(param) is types.DictType:
		return "&".join(("%s=%s" % (k, urllib2.quote(v)) for k, v in param.iteritems()))
	else:
		return urllib2.quote(param)

def mkcookie(name, value, domain=''):
	'''
	创建一个Cookie
	'''
	return cookielib.Cookie(version=None, name=name, value=value, port=None, port_specified=None, domain=domain, domain_specified=None, domain_initial_dot=None, path='/', path_specified=None, secure=None, expires=None, discard=None, comment=None, comment_url=None, rest=None, rfc2109=None)

def get_html_by_urldoc(doc):
	'''
	将一个urllib2.open()返回的doc读取为html文件文档(其实就是解码为字符串)
	'''
	try:
		contype = doc.info().getheader('Content-Type').lower()
	except:
		contype = 'application/x-www-form-urlencoded; charset=UTF-8'
	charset = None
	html = doc.read()
	chs = re.findall('charset\s*=\s*([^\s,^;]*)', contype)
	if chs and len(chs) > 0:
		charset = chs[0]
	else:
		chs = re.findall('charset\s*=\s*([^\s,^;,^"]*)', html)
		if chs and len(chs) > 0:
			charset = chs[0]
	if charset:
		charset = charset.lower()
		try:
			html = html.decode(charset)
		except:
			try:
				html = html.decode('utf-8')
			except:
				try:
					html = html.decode('gbk')
				except:
					raise Exception('decode error!')
	return html



