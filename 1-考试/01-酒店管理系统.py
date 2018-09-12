lists=[]
lists1=[]
mous=10#每秒10元
def menu():
	while True:
		print('　　　　　　　《欢迎来到酒店管理系统》')
		print('1、入住')
		print('2、离店')
		print('3、统计')
		print('4、退出')
		choose()


def choose():
	choose=input('请输入功能:')
	if choose.isdigit():
		choose=int(choose)
		if choose==1:
			add()
		elif choose==2:
			pop()
		elif choose==3:
			find()
		elif choose==4:
			exit()
			print('   欢迎下次再来^_^')

def add():
	d={}
	name=input('请输入名字:')
	d['name']=name
	while True:
		ID=input('请输入身份证号:')
		if len(ID)==18:
			d['ID']=ID
			break
		else:
			print('输入有误,请重新输入')
	lists.append(d)
	print(lists)
	print('添加成功')


def pop():
	name=input('请输入名字:')
	for i in lists:
		if name==i['name']:
			lists1.append(i)
	print('退店成功')


def find():
	print('总入住:',len(lists))
	print('离店:',len(lists1))

menu()

