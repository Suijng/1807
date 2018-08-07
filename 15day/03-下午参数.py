def hs(a,*sb,b=12,**wo):
	print(a)
	print(b)
	print(sb)
	print(wo)

	sum=0
	sum=sum+a
	sum=sum+b
	for j in sb:
		sum=sum+j

	for i in wo.values():
		sum=sum+i
	print(sum)

hs(1,2,3,4,5,b=20,m=12,n=22)




















