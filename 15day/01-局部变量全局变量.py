a=123

def hs():
	global a#局部变量改全局变量
	a=456
	print(a)

hs()
print(a)


list=['wo']

def lb():
	list.append('ni')#局部变量修改全局变量
	print(list)
lb()
print(list)









