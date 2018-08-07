list=[1,3,5,7,9,15,27,38,49]#有序排列
min=0#最小的索引
max=len(list)-1#最大索引
count=15#找到15的索引
while True:
	center=int((min+max)/2)
	if list[center]>count:
		max=center-1
	elif list[center]<count:
		max=center+1
	elif list[center]==count:
		print('索引是%d'%center)
		break


























