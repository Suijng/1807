lists=[]
while True:
	print('                《欢迎来到学生管理系统》')
	print('1,添加学生信息')
	print('2,查找学生信息')
	print('3,修改学生信息')
	print('4.删除学生信息')
	print('5,退出学生管理系统')
	sh=int(input('选择所需选项:'))

	if sh==1:
		mz=input('输入名字:')
		nl=input('输入年龄:')
		xb=input('输入性别:')
		dz=input('输入地址:')
		d={}
		d['name']=mz
		d['age']=nl
		d['sex']=xb
		d['dz']=dz
		lists.append(d)
		print(lists)

	elif sh==2:
		a=input('输入查找人的姓名:')
		for i in lists:
			if a==i['name']:
				print('学生姓名:%s\n学生年龄:%s\n学生性别:%s\n学生家庭地址%s'%(i['name'],i['age'],i['sex'],i['dz']))

	elif sh==3:
		b=input('输入要修改信息的姓名:')
		for j in lists:
			if b==j['name']:
				c=input('输入修改的项:')
				f=input('输入修改内容:')
				j[c]=f
				print(j)

	elif sh==4:
		e=input('输入要删除的姓名:')
		for n in lists:
			if e==n['name']:
				lists.remove(n)
				print(lists)

	elif sh==5:
		print('                     欢迎再次使用^-^')
		break

