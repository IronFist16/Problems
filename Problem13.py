max_x = 0
test = 2
count = 0
#mylist = []
upperRange = 1000000

while ( test < upperRange ):
	x = test
	i = 0
	cnt = 0
	while ( 1 ):
		if x == 1:
			#mylist.insert(i,x)
			cnt += 1
			if (count < cnt):
				max_x = test
				count = cnt
			break
		elif x % 2 == 0:
			#mylist.insert(i,x)
			cnt += 1
			x = x / 2
			i += 1
			continue
		else:
			#mylist.insert(i,x)
			cnt += 1
			x = 3*x + 1
			i += 1
			continue
	test += 1

print max_x
#print mylist
