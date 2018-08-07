while True:
	zh = int(input('输入账号:'))
	mm = input('输入密码:')
	je = int(input('输入金额:'))

	a = 300-je

	if zh==123 and mm=='zxc':
		if je < 300 and je >= 0:
			print('取出金额%d,所剩余额%d'%(je,a))
			
		elif (zh!=123) or (mm!='zxc'):
			print('非法账户')

		elif je<300 and je>=0:
			print(a)
		else:
			print('没钱取个毛线啊')
































