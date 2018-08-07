'''
#coding=utf-8
for i in range(1,101):
	if i%1==0 and i%i==0 : 
		print(i)
'''

for i in range(2,101):
	flag = 1
	for j in range(2,i):#验证的代码
		if i%j==0:
			flag = 0
			#break
	if flag==1:
		print(i)

























