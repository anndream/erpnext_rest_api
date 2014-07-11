# ERPNext GET/POST Request

## 1.Installation
 
### 1.1.Install python 2.7 in your system  ([**Windows**](http://www.anthonydebarros.com/2011/10/15/setting-up-python-in-windows-7/),[**Ubuntu**](http://askubuntu.com/questions/101591/how-do-i-install-python-2-7-2-on-ubuntu),[**MAC**](http://docs.python-guide.org/en/latest/starting/install/osx/))
### 1.2.Download and install easy install for Python ([**Windows**](http://adesquared.wordpress.com/2013/07/07/setting-up-python-and-easy_install-on-windows-7/),[**Ubuntu**](http://askubuntu.com/questions/27519/can-i-use-easy-install),[**MAC**](http://myadventuresincoding.wordpress.com/2011/09/11/python-upgrading-python-with-easy_install-pip-and-virtualenv-on-a-mac/))
### 1.3.To install python requests module(library) open command prompt/terminal and type "easy_install requests"
### 1.4.Clone/Download [**erpnext_rest_api**](https://github.com/Squadro/erpnext_rest_api)

## 2.Running

### 2.1. GET
#### 2.1.1.Get the list of documents of a documents of a particular doctype
Let us assume that we want to get the list of Item(doctype) in ERPNext
* Open the command prompt/terminal and navigate to the downloaded erpnext_rest_api folder 
*`python get_request.py "Item"`
* Response 
  `{"data":
      [{"name":"Kitchen rack"},
      {"name":"Iron rods"},
      {"name":"Book rack"},{"name":"Plywood"}]
  }`


#### 2.1.2.Get the specific information of a doctype
Let us assume that we want to get the information of Plywood in ERPNext
* Similarly as mentioned above Open the command prompt/terminal and navigate to the downloaded erpnext_rest_api folder
* ` python get_request.py "Item" "Plywood"`
* Response
  `{"data":
      {"name":"Plywood",
        "doctype":"Item",
        "last_purchase_rate":10.0,
        ......
        ......
      }
  }`


### 2.2.Post
#### 2.2.1.Create new element in a document
* Download post_request.py and run the script in terminal/command prompt by typing "C:\>cd Desktop{dir path of post_request.py}"  then "C:\Desktop>python post_request.py"
* In the script we are creating a new address. For that we are sending the data(Hash) to function "insert(data)".
* In data we mentioned "doctype"="Address","address_title":"Mr.TwoMonk","address_line1":"Vijayanagar","city":"BangLORE","phone":"012345678" these are the mandatory fields in ERPNext to create new address so we have to take care of these while creating new element in a doctype.
* If we want to add new element in a doctype(Address)/new address then just we change "address_title" in data
* If we miss the mandatory fields in data then we get Error 409


