```
r = requests.get()
r.status_code
r.headers['content-type']
r.encoding #utf-8
r.text
r.json
```
#####get query请求
```
payload = {'key1':'value1','key2':'value2'}
r = requests.get('https://xxxxxxxx',params=payload)
```

#####文件上传
```
files = {'file':open('xxx.xls','rb')}
r = requests.post(url,files=files)
```

#####普通的header
```
headers = ['user-agent':'my-app/0.01']
r = requests.get(url,headers=headers)
```


#####cookie
```
cookies = dict(cookies_are='working')
r = requests.get(url,cookies=cookies)
```