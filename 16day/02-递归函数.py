def text(a):
	if a==1:
		return a
	else:
		return a*text(a-1)
b=text(5)
print(b)


def text1(a):
	if a==100:
		return a
	else:
		return a+text1(a+1)
b=text1(1)
print(b)


def text2(a):
	if a==100:
		return a
	else:
		return a+text2(a+2)
b=text2(2)
print(b)


def text3(a):
	if a==99:
		return a
	else:
		return a+text3(a+2)
b=text3(1)
print(b)










