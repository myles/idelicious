#!/usr/bin/env python

import httplib, urllib

try:
	import simplejson
except ImportError:
	from django.utils import simplejson

class Delicious(object):
	def __init__(self, host, port=80, options=None):
		self.host = host
	
	def get_hotlist(self, count=15):
		r = self._get("", {'count': count})
		return self._render(r)
	
	def get_recent(self, count=15):
		r = self._get("recent", {'count': count})
		return self._render(r)
	
	def get_recent_by_tag(self, tag, count=15):
		r = self._get("tag/%s" % tag[0], {'count': count})
		return self._render(r)
	
	def get_popular(self, count=15):
		r = self._get("popular", {'count': count})
		return self._render(r)
	
	def get_popular_by_tag(self, tag, count=15):
		r = self._get("popular/%s" % tag[0], {'count': count})
		return self._render(r)
	
	def get_site_alerts(self):
		r = self._get('alerts')
		return self._render(r)
	
	def get_user(self, username, count=15):
		r = self._get('%s' % username, {'count': count})
		return self._render(r)
	
	def get_user_by_tag(self, username, tag, count=15):
		r = self._get('%s/%s' % (username, tag[0]), {'count': count})
		return self._render(r)
	
	def get_user_info(self, username, count=15):
		r = self._get("userinfo/%s" % username , {'count': count})
		return self._render(r)
	
	def get_user_tags(self, username, count=15):
		r = self._get('tags/%s' % username, {'count': count})
		return self._render(r)
	
	def get_url(self, url):
		r = self._get('url/%s' % url)
		return self._render(r)
	
	def get_urlinfo(self, url):
		r = self._get('urlinfo/%s' % url)
		return self._render(r)
	
	# Basic HTTP methods.
	
	def _connect(self):
		return httplib.HTTPConnection(self.host, port=80)
	
	def _get(self, uri, params={}):
		c = self._connect()
		headers = {}
		c.request("GET", "/v2/json/" + uri, urllib.urlencode(params), headers)
		return c.getresponse()
	
	def _render(self, results):
		json = results.read()
		return simplejson.loads(json)