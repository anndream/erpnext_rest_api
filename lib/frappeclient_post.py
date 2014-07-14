import requests
import json
import sys

class AuthError(Exception):
	pass

class FrappeException(Exception):
	pass

class FrappeClient(object):
	def __init__(self, url, username, password):
		self.session = requests.Session()
		self.url = url
		self.login(username, password)
	
	def login(self, username, password):
		r = self.session.post(self.url, data={
			'cmd': 'login',
			'usr': username,
			'pwd': password
		})

		if r.json().get('message') == "Logged In":
			print r					#prints Response HTTP code like 200,404,403,409
			print r.json()			#prints Response message
			return r.json()
		else:
			raise AuthError

	def insert(self, doc):
		res = self.session.post(self.url + "/api/resource/" + doc.get("doctype"),
			data={"data":json.dumps(doc)})
		print res.text					#prints Response message
		print res.status_code			#prints Response HTTP code like 200,404,403,409	
		return self.post_process(res)
	
	def post_process(self, response):
		try:
			rjson = response.json()
		except ValueError:
			print (response.text)
			raise

		if rjson and ("exc" in rjson) and rjson["exc"]:
			raise FrappeException(rjson["exc"])
		if 'message' in rjson:
			return rjson['message']
		elif 'data' in rjson:
			return rjson['data']
		else:
			return None
			


