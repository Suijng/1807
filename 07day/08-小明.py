sg = int(input('输入身高:'))
sj = int(input('输入身价:'))
yz = int(input('输入颜值分:')) 
if (sg>180 and yz>1000000 and sj>99) or (sj>1000000 and yz>99):
	print('高富帅')
elif yz>99:
	print('帅')
elif sg<160 and sj<100 and yz<60:
	print('矮穷矬')
else:
	print('傻吊')






























