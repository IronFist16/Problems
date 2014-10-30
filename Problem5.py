
x = 1
while(x >=1):
	if(all(not (x%y) for y in range(1,21))):
		print x
		break
	x += 1
