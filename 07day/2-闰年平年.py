n = int(input('输入年份:'))

if n%4 == 0 and n%100 != 0:
	print('闰年')
elif n %400 == 0:
	print('闰年')
else:
	print('平年')














