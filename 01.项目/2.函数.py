lists=[]
d={}

def error(yq):
	print('输入有误,请重新输入\t'+yq)

def add():#声明
	while True:
		name=input('请输入名字:')
		if len(name)>=2 and len(name)<=4:	
			d['name']=name
			break
		else:
			print('\n姓名必须大于2小于4\n')
	while True:
		phone=input('请输入手机号:')
		if phone.startswith('1') and len(phone)==11:
			d['phone']=phone
			break
		else:
			print('输入有误，请重新输入')
	while True:
		ID=input('请输入身份证号:')
		if len(ID)==18:
			d['ID']=ID
			break
		else:
			print('输入有误')
	lists.append(d)
	print(lists)


def find():
	find=input('请输入查找人的姓名:')
	for i in lists:
		if find==i['name']:
			print('\n实习生姓名:%s\n实习生手机号:%s\n实习生身份证号:%s\n'%(i['name'],i['phone'],i['ID']))
			break


def change():
	find=input('请输入实习生的名字:')
	for i in lists:
		if find==i['name']:
			print('\n实习生姓名:%s\n实习生手机号:%s\n实习生身份证号:%s\n'%(i['name'],i['phone'],i['ID']))	
			print('1、修改名字')
			print('2、修改手机号')
			print('3、修改身份证号')
			c=int(input('请选择修改的序号:'))
			if c==1:
				name=input('请输入新的名字:')
				i['name']=name
			elif c==2:
				phone=input('请输入新的手机号:')
				i['phone']=phone
			elif c==3:
				ID=input('请输入新的身份证号:')
				i['ID']=ID
		for k,v in i.items():
			print(k,v)


def pop():
	dell=input('输入要删除的姓名:')
	for j in lists:
		if dell==j['name']:
			lists.remove(j)
			print(lists)


def print_list():
	for i in lists:
		print(i)


def menu():
	while True:
		print('《欢迎来到练习生管理系统》'.center(50,' '))
		print('1、添加实习生信息')
		print('2、查找实习生信息')
		print('3、修改实习生信息')
		print('4、删除练习生信息')
		print('5、打印练习生信息')
		print('6、退出练习生系统')
		info()#调用选择功能的函数

def info():
	choose=int(input('选择所需选项:'))
	if choose==1:
		add()
	elif choose==2:
		find()
	elif choose==3:
		change()
	elif choose==4:
		pop()
	elif choose==5:
		print_list()
	elif choose==6:
		exit()
menu()













