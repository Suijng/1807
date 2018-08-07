i=1
c=0
while i<10:
	a=1
	while a<=i:
		c=a*i
		print('%d*%d=%d'%(i,a,c),end='')
		a=a+1
	print('')
	i=i+1
