import sys
sys.path.append('../lib/')
from frappeclient_get import *

#For ERPNext login
url = 'http://localhost:8080'
username = 'Administrator'
password =  'admin'
new_client = FrappeClient(url,username,password)
#doctype is a parameter which you send to server to GET response ie localhost:8080/api/resource/{doctype}
doctype = sys.argv[1]

#To GET response or to get an Item list from ERPNext
new_client.get_doc(doctype)
