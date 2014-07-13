# ERPNext GET/POST Request

## 1. Installation
 
### 1.1. Install python 2.7 in your system  ([**Windows**](http://www.anthonydebarros.com/2011/10/15/setting-up-python-in-windows-7/),[**Ubuntu**](http://askubuntu.com/questions/101591/how-do-i-install-python-2-7-2-on-ubuntu),[**MAC**](http://docs.python-guide.org/en/latest/starting/install/osx/))
### 1.2. Download and install easy install for Python ([**Windows**](http://adesquared.wordpress.com/2013/07/07/setting-up-python-and-easy_install-on-windows-7/),[**Ubuntu**](http://askubuntu.com/questions/27519/can-i-use-easy-install),[**MAC**](http://myadventuresincoding.wordpress.com/2011/09/11/python-upgrading-python-with-easy_install-pip-and-virtualenv-on-a-mac/))
### 1.3. To install python requests module(library) open command prompt/terminal and type "easy_install requests"
### 1.4. Clone/Download [**erpnext_rest_api**](https://github.com/Squadro/erpnext_rest_api)

## 2. Running

### 2.1. GET
#### 2.1.1. Get the list of documents of a documents of a particular doctype
Let us assume that we want to get the list of Item(doctype) in ERPNext
* Open the command prompt/terminal and navigate to the downloaded erpnext_rest_api folder 
* `python get_request.py "Item"`
* Response 
  `{"data":
      [{"name":"Kitchen rack"},
      {"name":"Iron rods"},
      {"name":"Book rack"},{"name":"Plywood"}]
  }`


#### 2.1.2. Get the specific information of a doctype
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


### 2.2. Post
#### 2.2.1. Create new element in a document
* Similarly as mentioned above Open the command prompt/terminal and navigate to the downloaded erpnext_rest_api folder
* ` python post_request.py `
* Response 
  `{"data":
     {"creation":"2014-07-13 22:04:35.098221",
       "doctype":"Address",
       "phone":"012345678",
       "owner":"Administrator",
       "city":"BangLORE",
       "address_line1":"Vijayanagar",
       "modified_by":"Administrator",
       "address_title":"Mr.Machha",
       "name":"Mr.GuruMachha-Billing",
       "country":"India",
       ......
       ......
     }
   }`
* By this you created new address in your ERPNext
* To create new element, open post_request.py in any editor and declare data as a dictionary like above and modified as you want
* Make sure to include mandatory fields in data



