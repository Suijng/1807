import random
while True:
	dn=random.randint(1,3)
	wj=int(input("请输入石头剪刀布"))
	if (wj==1 and dn==2)or(wj==2 and dn==3)or(wj==3 and dn==1):
		print("玩家赢")
	elif (wj==dn):
		print("平局")
	else:
		print("电脑赢") 




























