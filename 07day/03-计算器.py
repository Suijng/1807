while True:
	x = float(input('输入x值:\n'))
	y = float(input('输入y值:\n'))
	z = input('输入加减乘除:\n')

	a = x+y
	b = x-y
	c = x*y
	d = x/y

	if z == '+':
		print('x+y的值%d'%(a))
	elif z == '-':
		print('x-y的值%d'%(b))
	elif z == '*':
		print('x*y的值%d'%(c))
	elif z == '/':
		print('x/y的值%d'%(d))



















