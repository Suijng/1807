
'''
def bu():
	import random
	lists=[]
	for i in range(10):
		sj=random.randint(1,100)
		if sj not in lists:
			lists.append(sj)
	print(lists)
bu()
'''

import random
lists=[]
i=0
while i<=10:
	sj=random.randint(1,100)
	if sj in lists:
		i=i-1
	else:
		lists.append(sj)
	i=i+1
print(lists)







