import requests
import json

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
			print r				#prints Response HTTP code like 200,404,403,409
			print r.json()		#prints Response message
			return r.json()
		else:
			raise AuthError

#To GET List of an Item 
	def get_doc(self, doctype, name=None, filters=None):
		params = {}
		if filters:
			params["filters"] = json.dumps(filters)
		
		res = self.session.get(self.url + "/api/resource/" + doctype + "/",
			params=params)
		enable_cookie = requests.session()	
		print res.text						#prints Response message/content
		print res.status_code				#prints Response HTTP Code
		return self.post_process(res)

#To GET  an information about a single Item ie Plywood		
	def get_doc_information(self, doctype, name=None, filters=None):
		params = {}
		if filters:
			params["filters"] = json.dumps(filters)
		
		res = self.session.get(self.url + "/api/resource/" + doctype + "/"  + name,
			params=params)
		enable_cookie = requests.session()	
		print res.text
		print res.status_code
		return self.post_process(res)	

	def post_request(self, data):
		res = self.session.post(self.url, data=self.preprocess(data))
		res = self.post_process(res)
		return res

	def preprocess(self, params):
		"""convert dicts, lists to json"""
		for key, value in params.iteritems():
			if isinstance(value, (dict, list)):
				params[key] = json.dumps(value)
		return params

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
			
			
#For ERPNext login
url = 'http://localhost:8080'
username = 'Administrator'
password =  'admin'
get_request = FrappeClient(url,username,password)
#doctype is a parameter which you send to server to GET response ie localhost:8080/api/resource/{doctype}
doctype = "Item"
#To GET response or to get an Item list from ERPNext
get_request.get_doc(doctype)
#name is a parameter which you send to server to GET response ie localhost:8080/api/resource/{doctype}/{name}
name= "Plywood"
#To GET response(informaton) of an Item ie Plywood from ERPNext
get_request.get_doc_information(doctype,name)
