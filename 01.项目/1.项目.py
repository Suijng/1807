lists=[]
while True:
	print('                   《欢迎来到大家庭》')
	print('1.添加家人信息')
	print('2.查找家人信息')
	print('3.修改家人信息')
	print('4.删除家人信息')
	print('5.查看所有信息')
	print('6.退出家庭系统')
	choose=int(input('选择所需选项:'))


	d={}
	if choose==1:
		name=input('请输入名字:')
		d['name']=name
		phone=input('请输入手机号:')
		if phone.startswith('1') and len(phone)==11:
			d['phone']=phone
		else:
			print('输入有误,重新输入')
		ID=input('请输入身份证号:')
		if len(ID)!=18:
			print('输入有误')
		else:
			d['ID']=ID
		lists.append(d)
		print(lists)


	elif choose==2:
		find=input('输入查找人的姓名:')
		for i in lists:
			if find==i['name']:
				print('\n家人姓名:%s\n家人手机号:%s\n家人身份证号:%s\n'%(i['name'],i['phone'],i['ID']))	


	elif choose==3:
		find=input('输入家人的姓名:')
		for i in lists:
			if find==i['name']:
				print('\n家人姓名:%s\n家人手机号:%s\n家人身份证号:%s\n'%(i['name'],i['phone'],i['ID']))

				print('1.修改名字')
				print('2.修改手机号')
				print('3.修改身份证号')
				c=int(input('请选择修改的序号:'))
				if c==1:
					name=input('请输入新的名字:')
					i['name']=name
				elif c==2:
					phone=input('请输入新的手机号:')
					i['phone']=phone
				elif c==3:
					ID==input('请输入新的身份证号:')
					i['ID']=ID
				for k,v in i.items():
					print(k,v)


	elif choose==4:
		dell=input('输入要删除的姓名:')
		for j in lists:
			if dell==j['name']:
				lists.remove(j)
				print(lists)

	elif choose==5:
		for i in lists:
			print(i)


	elif choose==6:
		print('                     欢迎下次再来^_^')
		break














