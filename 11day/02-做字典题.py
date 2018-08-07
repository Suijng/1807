list=[]
for i in range(3):
	mz=input('输入名字:')
	nl=int(input('输入年龄:'))
	xb=input('输入性别:')
	print('')
	d={'name':mz,'age':nl,'sex':xb}
	list.append(d)
print(list)
print('')


for j in list:
	for n in j:
		print(j[n])

























