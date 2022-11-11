import requests
import shutil
import os
import json
import time

num=input("Enter The Number : " ) 

url = "https://api.eyecon-app.com/app/getnames.jsp?cli=91"+num+"&lang=en&is_callerid=true&is_ic=false&cv=vc_307_vn_2.0.307_a&requestApi=URLconnection&source=Other"

headers = {
    'accept': 'application/json',
    'e-auth-v': 'e1',
    'e-auth': '58e51d58-81e3-4155-a612-bd5987b8bb90',
    'e-auth-c': '38',
    'accept-charset': 'UTF-8',
    'content-type': 'application/x-www-form-urlencoded; charset=utf-8',
    'Host': 'api.eyecon-app.com',
    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'gzip',
    'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 10; HD1901 Build/QKQ1.190716.003)'
}

resp = requests.get(url=url, headers=headers)

resp = json.loads(resp.text)
if len(resp)>0:
	resp=resp[0]['name']
else:
	print("Nothing Found")
	exit()
print("Please Wait...")
time.sleep(2)
print("Looking Into The Database")
time.sleep(2)
print("By Our Database -  \nName Of The Number You Searched  Is : " , resp)


url="https://api.eyecon-app.com/app/pic?cli=91"+num+"&is_callerid=true&size=big&type=0&cancelfresh=0"


r = requests.get(url=url , headers=headers, allow_redirects=False)

if r.status_code == 200:
	os.mkdir(num)
	filename=str(num)+"/"+str(num)+".jpg"
	with open(filename, 'wb') as f:
		for chunk in r.iter_content():
			f.write(chunk)
		print("Voila ! Image Saved As " + num+".jpg")
		print("No Facebook Link Found")
if r.status_code == 302:
	os.mkdir(num)
	filename=str(num)+"/"+str(num)+".txt"
	s=open(filename, "w+")
	url=r.headers
	url=url['Location']
	linkfb=url[14:42:]
	linkfb="https://www."+linkfb
	s.write(linkfb)
	s.close()
	r = requests.get(url )
	if r.status_code == 200:
		filename=str(num)+"/"+str(num)+".jpg"
		with open(filename, 'wb') as f:
			for chunk in r.iter_content():
				f.write(chunk)
			print("Voila ! Image And The Link Of Facebook ID Saved In", num + " Folder")


if (r.status_code != 200 and r.status_code != 302):
	print("Oops ! Nothing Found ")