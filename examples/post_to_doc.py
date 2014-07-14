import sys
sys.path.append('../lib/')
from frappeclient_post import *

#For ERPNext login
url = 'http://localhost:8080'
username = 'Administrator'
password =  'admin'
new_client = FrappeClient(url,username,password)
#To pass parameters to ERPNext
data = {"doctype":"Address","address_title":"Mr.Guru","address_line1":"Vijayanagar","city":"BangLORE","phone":"012345678"} #To create new address in ERPNext
#To POST Request to ERPNext


new_client.insert(data)

