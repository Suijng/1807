a=0#记录登录失败的次数
while a<=3:
	a=a+1
	zh = input('输入账号:')
	mm = int(input('输入密码:'))
	if zh=='sj' and mm==123:
		print('登陆成功')
		yx = int(input('选择英雄范围 0=ADC 1=肉 3=法师\n:'))
		if yx == 0:
			print('鲁班大师')
		elif yx == 1:
			print('程咬金')
		elif yx == 3:
			print('王昭君')
	else:
		print('重新输入')






















