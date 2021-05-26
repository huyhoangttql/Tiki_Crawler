import requests
import json
headers = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}
r = requests.get('https://tiki.vn/api/v2/products?limit=48&include=advertisement&aggregations=1&trackity_id=c3c0f49b-531b-5326-1403-109ec7ddb123&category=1846&page=1&urlKey=laptop-may-vi-tinh-linh-kien',headers=headers)
data=r.json()

f = open('data.json','w+')
json.dump(data["data"],f,indent=4)
print(data)