
#c=j*15
#a=i*30

for i in range(15):
	a=i*30
	#print('鸭子%d+%d=%d'%(i,a,i+a*2))
	for j in range(20):
		c=j*15
		print('兔子%d+%d=%d'%(j,c,j+c),end='\t')
	print('鸭子%d+%d=%d'%(i,a,i+a))
























