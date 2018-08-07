list=[]
def add():
	while True:
		d={}
		ac=input('输入好友账号:')
		d['ac']=ac
		group=input('输入好友分组:')
		d['group']=group
		while True:
			name=input('输入好友备注:')
			if len(name)>=2 and len(name) <=4:
				d['name']=name
				break
			else:
				print('好友备注2~4为')
		list.append(d)
		print(list)
add()


