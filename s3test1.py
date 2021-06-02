import requests
import json

 

#login
url='https://10.1.13.245:8080/auth'
data={'password': 'admin', 'user_id': 'admin'}
header = {'Content-Type': 'application/json', 'accept': 'application/bigtera.vs.v1+json'}
session = requests.session()
res = session.post(url=url,data=json.dumps(data),headers=header,verify=False)
print(res.json)





#print s3 account

user_url = 'https://10.1.13.245:8080/s3/setting/account'
res = session.get(url=user_url,headers=header,verify=False)
account_list = res.json()
print(account_list)
j = json.dumps(account_list, indent = 10)
print(j, type(j))