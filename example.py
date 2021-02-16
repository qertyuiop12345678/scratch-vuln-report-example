# I modified some of the code for privacy.
import requests
import random,string
from threading import Thread
import time
import usernames

print('Originaly created by mat1 as a favorite bot.')

def randstr(length=8, chars=string.ascii_letters+string.digits):
	return ''.join([random.choice(chars) for i in range(length)])

def generateaccount():
	while True:
		createaccount()

def createaccount(classcode,classid):
	headers={'referer':'https://scratch.mit.edu/accounts/standalone-registration/','User-Agent':'Mozilla/5.0 (Linux; Android 7.0) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Klar/1.0 Chrome/58.0.3029.83 Mobile Safari/537.36'}
	username=usernames.create()
	password=randstr(10)
	theemail=""
	if theemail=="":
		email=randstr(7)+'@'+randstr(5)+'.com'
	else:
		email=theemail
	try:
		r=requests.get('https://scratch.mit.edu/csrf_token/',headers=headers)
	except:
		print('Something bad happened')
		return
	cookies=dict(r.cookies)
	csrftoken=cookies['scratchcsrftoken']
	payload={'username':username,'password':password,'birth_month':1,'birth_year':2000,'gender':'male','country':'United States','is_robot':'false','csrfmiddlewaretoken':csrftoken,"classroom_token":classcode,'classroom_id':classid}
	try:
		r=requests.post('https://scratch.mit.edu/classes/register_new_student/',payload,headers=headers,cookies=cookies)
		print(r.text)
		rj = r.json()[0]
		if r.text == '''[{"msg": "too many students", "errors": {"__all__": ["too many students"]}, "success": false}]''':
		 keynext()
		 print('ddsdds')
	except:
		return 'fff'
	f=open('accounts.txt', 'a+')
	try:
	 if r.json()[0]['success'] == True:
	  userinfo={}
	  userinfo['username']=username	
	  userinfo['email']="null"
	  userinfo['password']=password
	  f.write(str(userinfo)+'\n')
	  f.close()
	  print(len(open('accounts.txt', 'r').read().splitlines()))
	except:
	  print('error')
#for i in range(64):
#	thread = Thread(target = generateaccount,args=('usernamesssdccdc'))
#	thread.start()

d  = open('keys.txt').read().splitlines()
ak = len(d)
for line in d:
  key = line.split(':')

def keynext():
  global key,d,ak
  for line in d:
    if line == key[0]+':'+key[1]:
      pass
  else:
    print(line)
    key = line.split(':')

dump = open('accountname.txt')
while True:
  for line in d:
    key = line.split(':')
    createaccount(key[0],key[1])
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	return "just to keep u up all night :)"

app.run('0.0.0.0',8080)
