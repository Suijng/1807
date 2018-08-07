import random
a = random.randint(0,100)

aa=0
while True:
	aa=aa+1
	if aa>10:
		break
	yh = int(input('请猜数字:'))
	if yh<a:
		print('猜小了')
	elif yh>a:
		print('猜大了')
	else:
		print('猜对了')
		break

