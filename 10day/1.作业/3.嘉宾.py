list=['马成超','张自豪','袁玉雨','白明睿']
for i in list:
	print('欢迎%s来参加我的婚礼'%i)
print('')


print('张自豪上天来不了了,需要更换嘉宾名单为:王玉成')
list.pop(1)
list.insert(1,'王玉成')
for j in list:
	print(j)
print('')


print('我找到更大的桌,都来吧')
list.insert(0,'芳芳')
list.insert(2,'大神')
list.append('马欢丽')
for n in list:
	print(n)
print('')


print('餐桌因无法送达,只能邀请两位嘉宾')
list.pop(0)
list.pop(1)
list.pop(1)
list.pop(1)
list.pop()
for m in list:
	print('%s 你很受欢迎'%m)
print('')


del list[0]
del list[0]
print(list)


