'''
def clum1(xyz):
	#print(z) 打印匿名函数地址
	ret=z(x,y)
	return ret
#ret=clum1(1,2,lambda x,y:x+y)
#print(ret)
#print(clum)#打印函数地址
ret=clum1(1,2,lambda x,y:x-y)
print(ret)
list=[]
'''
def add():
	for i in range(3):
		l=[]
		for j in range(3):
			grade=dloat(input('输入成绩'))
			l.append(grade)
		list.append(l)
	print(list)


maxgrade=0
mp=0
def mmax():
	global maxgrade
	global mp
	for p,i in enumerate(list):
		if sum(i)>maxgrade:
			maxgrade=sum(i)
			mp=p
	print(maxgrade)
	print(mp)
	print('平均分是%.02f'%(maxgrade/3))
	print(list[mp][0],list[mp][1],list[mp][2])














