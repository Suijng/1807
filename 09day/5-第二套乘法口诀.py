i=1
while i<=9:
	j=1
	while j<=i:
		a=j*i
		print('%d*%d=%d'%(j,i,a),end='\t')
		j=j+1
	print('')
	i=i+1
